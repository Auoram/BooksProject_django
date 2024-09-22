from django.shortcuts import render
from .models import Books,Author

# Create your views here.

def index(request):
    return render(request,'books/index.html' , {
        'books':Books.objects.all()
    })