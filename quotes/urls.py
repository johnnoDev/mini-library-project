from django.urls import path
from . import views

urlpatterns = [
    path("<int:day>", views.days_week_with_number),
    path("<str:day>", views.days_week, name="day-quote")  # /quotes/friday
]
