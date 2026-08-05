# ────────────────────────────────
# 0. Imports y utilidades
# ────────────────────────────────
import random
import itertools
from datetime import date, timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model

from library.models import (
    Author, Genre, Book, BookDetail,
    Review, Loan, Recommendation
)

User = get_user_model()

# ────────────────────────────────
# 1. Usuarios (20)
# ────────────────────────────────
users = [
    User(username=f"user{i}", email=f"user{i}@demo.com")
    for i in range(1, 21)
]
# Hash de password seguro:
for u in users:
    u.set_password("pass1234")
User.objects.bulk_create(users)

users = list(User.objects.all())   # recargamos con IDs

# ────────────────────────────────
# 2. Autores (20)
# ────────────────────────────────
authors = [
    Author(name=f"Autor {i}", birth_date=date(1950+i, 1, 1))
    for i in range(1, 21)
]
Author.objects.bulk_create(authors)
authors = list(Author.objects.all())

# ────────────────────────────────
# 3. Géneros (20)
# ────────────────────────────────
genres = [
    Genre(name=gn) for gn in [
        "Ficción", "Drama", "Ciencia Ficción", "Distopía",
        "Aventura", "Romance", "Misterio", "Histórico",
        "Poesía", "Fantástico", "Biografía", "Ensayo",
        "Horror", "Thriller", "Policíaco", "Humor",
        "Infantil", "Juvenil", "Filosofía", "Autoayuda"
    ]
]
Genre.objects.bulk_create(genres)
genres = list(Genre.objects.all())

# ────────────────────────────────
# 4. Libros (20)
# ────────────────────────────────
books = []
for i in range(1, 21):
    books.append(
        Book(
            title=f"Libro {i}",
            publication_date=date(2000+i, 6, 1),
            author=random.choice(authors),
            pages=random.randint(150, 600),
            isbn=f"ISBN-{1000+i}"
        )
    )
Book.objects.bulk_create(books)
books = list(Book.objects.all())

# Many-to-Many (asigna 2 géneros aleatorios a cada libro)
for book in books:
    book.genres.add(*random.sample(genres, 2))

# ────────────────────────────────
# 5. BookDetail (20)  – uno por libro
# ────────────────────────────────
details = []
for book in books:
    details.append(
        BookDetail(
            book=book,
            summary=f"Resumen de {book.title}",
            cover_url=f"https://picsum.photos/seed/{book.id}/200/300",
            language=random.choice(["Español", "Inglés", "Francés"])
        )
    )
BookDetail.objects.bulk_create(details)

# ────────────────────────────────
# 6. Reviews (20)
# ────────────────────────────────
reviews = []
for i in range(20):
    reviews.append(
        Review(
            user=random.choice(users),
            book=random.choice(books),
            rating=random.randint(1, 5),
            text="Excelente lectura" if i % 2 == 0 else "Interesante pero mejorable"
        )
    )
Review.objects.bulk_create(reviews)

# ────────────────────────────────
# 7. Loans (20)  – la mitad devueltos
# ────────────────────────────────
loans = []
today = timezone.now()
for i in range(20):
    loan_date = today - timedelta(days=random.randint(1, 60))
    returned = i % 2 == 0
    loans.append(
        Loan(
            user=random.choice(users),
            book=random.choice(books),
            loan_date=loan_date,
            is_returned=returned,
            return_date=loan_date + timedelta(days=15) if returned else None
        )
    )
Loan.objects.bulk_create(loans)

# ────────────────────────────────
# 8. Recommendations (20)
# ────────────────────────────────
recs = []
book_cycle = itertools.cycle(books)
for i in range(20):
    recs.append(
        Recommendation(
            user=random.choice(users),
            book=next(book_cycle),
            note="¡Tienes que leerlo!"
        )
    )
Recommendation.objects.bulk_create(recs)

print("✅ ¡20 registros creados en cada tabla!")