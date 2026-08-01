from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("index/<int:day>/", views.days_week_with_number),
    path("index/<str:day>/", views.days_week, name="day-quote")  # /quotes/friday
]
