from django.contrib import admin
from django.urls import path
from . import views

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
] 
