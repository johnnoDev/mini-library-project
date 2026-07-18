from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello_fbv/', views.hello, name='hello_fbv'),
    path('hello_cbv/', views.Hello.as_view(), name='hello_cbv'),
    path('welcome/', views.Welcome.as_view(), name='welcome'),
    path('authors/', views.AuthorListView.as_view(), name='author_list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author')
]

