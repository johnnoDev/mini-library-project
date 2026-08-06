from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Author, Genre, Book

# Create your views here.
    


def index(request):
    # try:
        books = Book.objects.all()
        author_id = request.GET.get('author') # parametro (?author=)
        genre_id = request.GET.get('genre') # parametro (...&genre=)
        
        if author_id:
            books = books.filter(author_id=author_id)
            
        if genre_id:
            books = books.filter(genres__id_genre=genre_id)
        
        return render(request, 'library/index.html', {
            'author': author_id,
            'books': books, 
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
