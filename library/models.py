from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Author(models.Model):
    id_author = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Genre(models.Model):
    id_genre = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    id_book = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    publication_date = models.DateField(null=True, blank=True)
    pages = models.IntegerField(default=0)
    isbn = models.CharField(max_length=30)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='books'
    )
    genres = models.ManyToManyField(Genre, related_name='books') # Tabla intermedia
    recommended_by = models.ManyToManyField(
        get_user_model(), through="Recommendation", related_name='recommendations',
    )    


    class Meta: 
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
    
    def __str__(self):
        return self.title
    
# Tabla 1:1
class BookDetail(models.Model):
    id_book_detail = models.AutoField(primary_key=True)
    summary = models.TextField()
    cover_url = models.CharField(max_length=200)
    language = models.CharField(max_length=50)
    book = models.OneToOneField(
        Book, on_delete=models.CASCADE, related_name='detail'
    )
    
class Review(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='reviews'
    )
    rating = models.PositiveIntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user} -> {self.book} ({self.rating} / 5)'
    
class Loan(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='loans'
    )
    load_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user} -> {self.book} Estado=({"Devuelto" if self.is_returned else "Prestado"})'
    
class Recommendation(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='recommendations'
    )
    recommended_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()
    
    class Meta:
        unique_together = ("user", "book")