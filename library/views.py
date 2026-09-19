from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound, HttpResponseForbidden
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import ReviewSimpleForm, ReviewForm
from .models import Author, Genre, Book, Review
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.
User = get_user_model()

@login_required
def index(request):
    # try:
        books = Book.objects.all()
        query = request.GET.get('query_search')

        date_start = request.GET.get('start')
        date_end = request.GET.get('end')
        book_id_recommend = request.session.get('last_viewed_book')
        
        if query:
            books = books.filter(
                Q(title__icontains=query) | Q(author__name__icontains=query)
            )

        if date_start and date_end:
            books = books.filter(
                publication_date__range=[date_start, date_end] # Rango de fechas
            )

        
        # Iniciar el paginador (e.j 5 libros por pagina)
        paginator = Paginator(books, 5)
        
        # Obtener el número de página actual desde los parámetros de la URL (?page=2)
        page_number = request.GET.get('page')
        
        # Obtener los objetos de la página solicitada
        page_obj = paginator.get_page(page_number)

        query_params = request.GET.copy()

        if 'page' in query_params:
            query_params.pop('page')

        query_string = query_params.urlencode()

        if book_id_recommend:
            try: 
                last_book = Book.objects.get(pk=book_id_recommend)
            except Book.DoesNotExist:
                last_book = None
        else:
            last_book = None
        
        return render(request, 'library/index.html', {
            'page_obj': page_obj, 
            'query': query,
            'query_string': query_string,
            'last_book': last_book
        })
    # except Exception:
    #     return HttpResponseNotFound('Página no encontrada')

@permission_required('library.add_review')
def add_review(request, book_id):
    book = get_object_or_404(Book, id_book=book_id)
    form = ReviewForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            would_recommend = form.cleaned_data.get('would_recommend')
            if would_recommend:
                messages.success(request, 'Gracias por la reseña y por recomendar el libro!!')
            else:
                messages.success(request, 'Gracias por la reseña.')
            return redirect('recommend_book', book_id=book.id_book)
        
        else:
            messages.error(request, 'Error en la reseña', 'danger')

    return render(request, 'library/add_review.html', {
        "book": book,
        "form": form
    })

# TemplateView
class WelcomeTemplateView(TemplateView):
    template_name = 'library/welcome.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context['total_books'] = Book.objects.count()
        return context
    
# Models: Book --------------------------
class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'
    paginate_by = 5
    
class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'
    
    def get(self, request, *args, **kwargs):
        if request.user.has_perm('library.view_book'):
            response = super().get(request, *args, **kwargs)
            request.session['last_viewed_book'] = self.object.id_book
            return response
        else:
            return HttpResponseForbidden('Contenido no disponible (No tienes permisos)')

# --------- Review
class ReviewCreateView(CreateView):
    model = Review
    template_name = 'library/add_review.html'
    form_class = ReviewForm
    
    def form_valid(self, form):
        book_id = self.kwargs.get('pk')
        book = Book.objects.get(pk=book_id)
        form.instance.book = book
        form.instance.user_id = self.request.user.id
        messages.success(self.request, 'Gracias por su reseña')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'pk': self.kwargs.get('pk')})
        
class ReviewUpdateView(UpdateView):
    model = Review
    template_name = 'library/add_review.html'
    form_class = ReviewForm
    
    def get_queryset(self):
        return Review.objects.filter(user_id=self.request.user.id)
    
    def form_valid(self, form):
        messages.success(self.request, 'Gracias por su reseña')
        return super().form_valid(form)
    
    def get_success_url(self):
        review = Review.objects.get(pk=self.kwargs.get('pk'))
        book_id = review.book.id_book
        return reverse_lazy('book_detail', kwargs={'pk': book_id})

class ReviewDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'library.delete_review'
    model = Review
    template_name = 'library/review_confirm_delete.html'
    success_url = reverse_lazy('book_list')
    context_object_name = 'review'

    def get_queryset(self):
        return Review.objects.filter(user_id=self.request.user.id)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'La reseña fue eliminada con exito!')
        return super().delete(request, *args, **kwargs)

# ListView (READ)
class AuthorListView(ListView):
    model = Author
    template_name = 'library/author_list.html'
    
"""
DetailView — la "R" singular
Es la vista para ver un solo autor (por ejemplo al hacer click en un nombre de la lista). El patrón es casi idéntico al ListView:
"""

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'library/author_detail.html'

class AuthorCreateView(CreateView):
    model = Author
    fields = ['name', 'birth_date']
    success_url = reverse_lazy('author_list')

class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['name', 'birth_date']
    success_url = reverse_lazy('author_list')

class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('author_list')
    


# -----------------------------------------------------

# READ

class GenreListView(ListView):
    model = Genre
    template_name = 'library/genre_list.html'
    
class GenreDetailView(DetailView):
    model = Genre
    template_name = 'library/genre_detail.html'
    
# CREATE
class GenreCreateView(CreateView):
    model = Genre
    fields = ['name']
    success_url = reverse_lazy('genre_list')
        
# UPDATE
class GenreUpdateView(UpdateView):
    model = Genre
    fields = ['name']
    success_url = reverse_lazy('genre_list')

# DELETE
class GenreDeleteView(DeleteView):
    model = Genre
    success_url = reverse_lazy('genre_list')

def counter_visit(request):
    visit = request.session.get('visitas', 0)
    visit += 1
    request.session['visitas'] = visit
    request.session.set_expiry(0)
    return HttpResponse(f"Has visitado está página {visit} veces")