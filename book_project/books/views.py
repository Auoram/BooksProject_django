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
            form.save()
            return render(request, 'books/add.html', {
                'form': BooksForm(),
                'success': True
            })
    else:
        form = BooksForm()

    return render(request, 'books/add.html', {
        'form': form
    })

def edit(request, id):
    book = Books.objects.get(pk=id)
    if request.method == 'POST':
        form = BooksForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return render(request, 'books/edit.html', {
                'form': form,
                'success': True
            })
    else:
        form = BooksForm(instance=book)

    return render(request, 'books/edit.html', {
        'form': form
    })

def delete(request, id):
    if request.method == 'POST':
        book = Books.objects.get(pk=id)
        book.delete()
    return HttpResponseRedirect(reverse('books:index'))

def all_authors(request):
    authors = Author.objects.all()
    return render(request, 'books/authors.html', {'authors': authors})