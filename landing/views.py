from django.shortcuts import render
from datetime import date

# Create your views here.

def home(request):
    today = date.today()
    return render(request, 'landing/landing.html', {
        "name": "Johnny",
        "age": 21,
        "date": today,
    })