from django.contrib import admin
from .models import Author, Book, Genre, BookDetail, Review, Loan
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

User = get_user_model()

class LoanInline(admin.TabularInline):
    model = Loan
    extra = 1
    
class CustomUserAdmin(BaseUserAdmin):
    inlines = [LoanInline]
    list_display = ('username', 'email')

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

class BookDetailInline(admin.StackedInline):
    model = BookDetail
    can_delete = False
    verbose_name_plural = 'Detalle del libro'

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [ReviewInline, BookDetailInline]
    list_display = ('title', 'author', 'publication_date', 'isbn') # Columnas que se mostrarán en admin/.../book
    search_fields = ('title', 'author__name') # Crea un campo de búsqueda con los campos asignados
    list_filter = ('author', 'genres', 'publication_date') # Crea un panel lateral derecho con filtros rápidos
    ordering = ['publication_date'] # Define el orden predeterminado en el que se mostrarán los registros al cargar la página
    date_hierarchy = 'publication_date' # Agrega una barra de navegación basada en fechas en la parte superior de la vista de lista
    fieldsets = (
        ('informacion general', {
            'fields': ('title', 'author', 'publication_date', 'genres')
        }),
        ('Detalles', {
            'fields': ('isbn', 'pages'),
            'classes': ('collapse',) # Oculta la información opcionalmente
        })
    )
    
@admin.register(Loan)
class LoanAdmin((admin.ModelAdmin)):
    list_display = ('user', 'book', 'load_date', 'return_date', 'is_returned')




admin.site.register(Author)
# admin.site.register(Book, BookAdmin)
admin.site.register(Genre)
admin.site.register(BookDetail)
admin.site.register(Review)
# admin.site.register(Loan)

try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

admin.site.register(User, CustomUserAdmin)