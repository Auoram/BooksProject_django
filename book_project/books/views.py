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
        form = BooksForm(request.POST)
        if form.is_valid():
            new_book_isbn = form.cleaned_data['isbn']
            new_book_name = form.cleaned_data['book_name']
            new_book_genre = form.cleaned_data['genre']
            new_book_author = form.cleaned_data['author']
            new_book_date = form.cleaned_data['publication_date']
            new_book_language = form.cleaned_data['language']
            new_book_cover = form.cleaned_data['cover_image']
            new_book_available = form.cleaned_data['available']
            new_book_rating = form.cleaned_data['rating']

            new_book = Books(
                isbn = new_book_isbn,
                book_name = new_book_name,
                genre = new_book_genre,
                author = new_book_author,
                publication_date = new_book_date,
                language = new_book_language,
                cover_image = new_book_cover,
                available = new_book_available,
                rating = new_book_rating
            )
            new_book.save()
            return render(request,'books/add.html',{
                'form':BooksForm(),
                'success':True
            })
        
    else:
        form = BooksForm()
    return render(request,'books/add.html',{
        'form':BooksForm()
    })