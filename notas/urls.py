from django.urls import path, include
from . import views

urlpatterns = [
    path('counter/', views.counter_visit, name='counter_visit')
]
