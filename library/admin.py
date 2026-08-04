from django.contrib import admin
from .models import Author, Book, Genre, BookDetail, Review, Loan

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'isbn') # Columnas que se mostrarán en admin/.../book
    search_fields = ('title', 'author__name') # Crea un campo de búsqueda con los campos asignados
    list_filter = ('author', 'genres', 'publication_date') # Crea un panel lateral derecho con filtros rápidos
    ordering = ['publication_date'] # Define el orden predeterminado en el que se mostrarán los registros al cargar la página
    date_hierarchy = 'publication_date' # Agrega una barra de navegación basada en fechas en la parte superior de la vista de lista

admin.site.register(Author)
# admin.site.register(Book, BookAdmin)
admin.site.register(Genre)
admin.site.register(BookDetail)
admin.site.register(Review)
admin.site.register(Loan)
