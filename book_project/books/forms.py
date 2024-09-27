from django import forms
from .models import Books

class BooksForm(forms.Media):
    class Meta:
        model = Books
        fields = ['__all__']
        labels = {
            'isbn':'ISBN',
            'book_name':'Book Name',
            'genre':'Genre',
            'author':'Author',
            'publication_date':'Publication Date',
            'language':'Language',
            'cover_image':'Book Cover',
            'available':'Available',
            'rating':'Rating',
        }
        widgets = {
            'isbn': forms.NumberInput(attrs={'class':'form-control'}),
            'book_name': forms.TextInput(attrs={'class':'form-control'}),
            'genre':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'publication_date':forms.DateInput(attrs={'class':'form-control'}),
            'language':forms.TextInput(attrs={'class':'form-control'}),
            'cover_image': forms.ImageField(),
            'available':forms.BooleanField(),
            'rating': forms.NumberInput(attrs={'class':'form-control'}),
        }