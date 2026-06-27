# Datos de prueba — Mini Library

---

## Autores (Author)

| id_author | name                    | birth_date |
|-----------|-------------------------|------------|
| 1         | Gabriel García Márquez  | 1927-03-06 |
| 2         | Isabel Allende          | 1942-08-02 |
| 3         | Jorge Luis Borges       | 1899-08-24 |
| 4         | Mario Vargas Llosa      | 1936-03-28 |
| 5         | Julio Cortázar          | 1914-08-26 |

---

## Géneros (Genre)

| id_genre | name              |
|----------|-------------------|
| 1        | Realismo mágico   |
| 2        | Novela histórica  |
| 3        | Fantasía          |
| 4        | Cuento            |
| 5        | Política          |

---

## Libros (Book)

| id_book | title                             | publication_date | pages | isbn              | author (id) |
|---------|-----------------------------------|------------------|-------|-------------------|-------------|
| 1       | Cien años de soledad              | 1967-05-30       | 432   | 978-0-06-088328-7 | 1           |
| 2       | El amor en los tiempos del cólera | 1985-09-05       | 368   | 978-0-14-028525-5 | 1           |
| 3       | La casa de los espíritus          | 1982-10-01       | 448   | 978-0-15-615985-0 | 2           |
| 4       | El aleph                          | 1949-06-01       | 224   | 978-0-14-028805-8 | 3           |
| 5       | Ficciones                         | 1944-01-01       | 208   | 978-0-8021-3010-6 | 3           |
| 6       | La ciudad y los perros            | 1963-10-01       | 360   | 978-84-322-0247-0 | 4           |
| 7       | Rayuela                           | 1963-06-28       | 736   | 978-84-376-0049-4 | 5           |

---

## Relación Libro — Género (Book_genres)

| id_book | id_genre |
|---------|----------|
| 1       | 1        |
| 1       | 4        |
| 2       | 1        |
| 3       | 2        |
| 3       | 1        |
| 4       | 4        |
| 4       | 3        |
| 5       | 4        |
| 5       | 3        |
| 6       | 5        |
| 6       | 2        |
| 7       | 3        |

---

## Detalle de Libro (BookDetail)

| id_book_detail | summary                                                                                                          | cover_url                                                          | language | book (id) |
|----------------|------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|----------|-----------|
| 1              | La historia de la familia Buendía a lo largo de siete generaciones en el pueblo ficticio de Macondo.             | https://covers.openlibrary.org/b/id/8228691-L.jpg                  | Español  | 1         |
| 2              | La historia de amor entre Florentino Ariza y Fermina Daza, separados en la juventud y reunidos en la vejez.     | https://covers.openlibrary.org/b/id/8231432-L.jpg                  | Español  | 2         |
| 3              | Saga familiar que narra la historia de Chile a través de tres generaciones de la familia Del Valle–Trueba.       | https://covers.openlibrary.org/b/id/8236884-L.jpg                  | Español  | 3         |
| 4              | Colección de cuentos fantásticos que exploran el infinito, los laberintos y la identidad.                        | https://covers.openlibrary.org/b/id/8222155-L.jpg                  | Español  | 4         |
| 5              | Dos colecciones de relatos breves que mezclan lo fantástico con lo real en mundos imaginarios y laberínticos.    | https://covers.openlibrary.org/b/id/8218966-L.jpg                  | Español  | 5         |
| 6              | Retrató la vida de los cadetes en el Colegio Militar Leoncio Prado y la violencia que genera la disciplina castrense. | https://covers.openlibrary.org/b/id/9252962-L.jpg             | Español  | 6         |
| 7              | Una novela experimental que sigue a Horacio Oliveira en París y Buenos Aires, desafiando la narrativa lineal.   | https://covers.openlibrary.org/b/id/8236067-L.jpg                  | Español  | 7         |
