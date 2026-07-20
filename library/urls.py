from django.contrib import admin
from django.urls import path
from . import views, views_fbv

urlpatterns = [
    path('', views.WelcomeTemplateView.as_view(), name='welcome_template'),
    path('authors/', views.AuthorListView.as_view(), name='author_list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('authors/new/', views.AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:pk>/edit/', views.AuthorUpdateView.as_view(), name='author_update'),
    path('authors/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author_delete'),
    path('genres/', views.GenreListView.as_view(), name='genre_list'),
    path('genres/<int:pk>/', views.GenreDetailView.as_view(), name='genre_detail'),
    path('genres/new/', views.GenreCreateView.as_view(), name='genre_create'),
    path('genres/<int:pk>/edit/', views.GenreUpdateView.as_view(), name='genre_update'),
    path('genres/<int:pk>/delete/', views.GenreDeleteView.as_view(), name='genre_delete'),
    # ------------------------
    # FBV
    path('fbv/authors/', views_fbv.author_list_fbv, name='author_list_fbv'),
    path('fbv/authors/<int:pk>/', views_fbv.author_detail_fbv, name='author_detail_fbv'),
    path('fbv/authors/new/', views_fbv.author_create_fbv, name='author_create_fbv'),
    path('fbv/authors/<int:pk>/edit/', views_fbv.author_update_fbv, name='author_update_fbv'),
    path('fbv/authors/<int:pk>/delete/', views_fbv.author_delete_fbv, name='author_delete_fbv'),
    
] 
