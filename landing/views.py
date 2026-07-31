from django.shortcuts import render
from datetime import date
from django.http import HttpResponse

# Create your views here.

def home(request):
    today = date.today()
    stack = [
        {'id':'python', 'name':'Python'},
        {'id': 'ruby', 'name':'Ruby'},
        {'id': 'javascript', 'name':'JavaScript'},
        {'id': 'php', 'name': 'PHP'}
        ]
    return render(request, 'landing/landing.html', {
        "name": "XD",
        "age": 21,
        "date": today,
        "lenguajes": stack,
    })
    
def stack_detail(request, tool):
    return HttpResponse(f"Tecnlogías: {tool}")