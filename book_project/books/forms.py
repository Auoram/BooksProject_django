from django import forms
from .models import Books,Author

class BooksForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        widget=forms.Select(attrs={'class': 'block w-full px-3 py-2 border border-gray-300 rounded-lg text-sm focus:ring-amber-500 focus:border-amber-500',}),
        empty_label="Select Author",
        label="Author"
    )
    class Meta:
        model = Books
        fields = '__all__'
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
            'isbn': forms.NumberInput(attrs={'class': 'block w-full px-3 py-2 border border-gray-300 rounded-lg text-sm focus:ring-amber-500 focus:border-amber-500',}),
            'book_name': forms.TextInput(attrs={'class': 'block w-full px-3 py-2 border border-gray-300 rounded-lg text-sm focus:ring-amber-500 focus:border-amber-500',}),
            'genre':forms.TextInput(attrs={'class': 'block w-full px-3 py-2 border border-gray-300 rounded-lg text-sm focus:ring-amber-500 focus:border-amber-500',}),
            'publication_date':forms.DateInput(attrs={'class': 'block w-full px-3 py-2 border border-gray-300 rounded-lg text-sm focus:ring-amber-500 focus:border-amber-500','type': 'date'}),
            'language':forms.TextInput(attrs={'class': 'block w-full px-3 py-2 border border-gray-300 rounded-lg text-sm focus:ring-amber-500 focus:border-amber-500',}),
            'cover_image': forms.ClearableFileInput(attrs={'class': 'block w-full px-3 py-2 text-sm',}),
            'available': forms.CheckboxInput(attrs={'class': 'h-4 w-4 text-amber-600 border-gray-300 rounded focus:ring-amber-500',}),
            'rating': forms.NumberInput(attrs={'class': 'block w-full px-3 py-2 border border-gray-300 rounded-lg text-sm focus:ring-amber-500 focus:border-amber-500',}),
        }