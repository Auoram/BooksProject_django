from django.shortcuts import render
from .models import Books,Author
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import BooksForm
# Create your views here.

def index(request):
    return render(request,'books/index.html' , {
        'books':Books.objects.all()
    })

def view_books(request, id):
    book = Books.objects.get(pk= id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # You don't need to manually assign fields; the form will handle this
            return render(request, 'books/add.html', {
                'form': BooksForm(),
                'success': True
            })
    else:
        form = BooksForm()

    return render(request, 'books/add.html', {
        'form': form
    })