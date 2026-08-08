from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Author, Genre, Book

# Create your views here.
    


def index(request):
    # try:
        books = Book.objects.all()
        query = request.GET.get('query_search')

        date_start = request.GET.get('start')
        date_end = request.GET.get('end')
        
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

        return render(request, 'library/index.html', {
            'page_obj': page_obj, 
            'query': query,
            'query_string': query_string,
        })
    # except Exception:
    #     return HttpResponseNotFound('Página no encontrada')

# TemplateView
class WelcomeTemplateView(TemplateView):
    template_name = 'library/welcome.html'
    
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
