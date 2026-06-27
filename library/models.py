from django.db import models

# Create your models here.
class Author(models.Model):
    id_author = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    
class Genre(models.Model):
    id_genre = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    
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
    

# Tabla intermedia

# class BookGenre(models.Model):
#     id_book_genre = models.AutoField(primary_key=True)
#     book = models.ForeignKey(
#         Book, on_delete=models.CASCADE, related_name='genres'
#     )
#     genre = models.ForeignKey(
#         Genre, on_delete=models.PROTECT, related_name='books'
#     )