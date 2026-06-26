from django.db import models

# Create your models here.
class Author(models.Model):
    author = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    
class Book(models.Model):
    book = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    publication_date = models.DateField(null=True, blank=True)
    pages = models.IntegerField(default=0)
    isbn = models.CharField(max_length=30)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='books'
    )
    
class Genre(models.Model):
    genre = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

# Tabla intermedia

class BookGenre(models.Model):
    book_genre = models.AutoField(primary_key=True)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='genres'
    )
    genre = models.ForeignKey(
        Genre, on_delete=models.PROTECT, related_name='books'
    )