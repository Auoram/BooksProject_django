from django.db import models

# Create your models here.

class Author(models.Model):
    full_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    awards = models.TextField(null=True, blank=True)
    biography = models.TextField(null=True, blank=True)


class Books(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    book_name = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    language = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)
    available = models.BooleanField(default=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

    def get_books_by_author(cls, author):
        return cls.objects.filter(author=author)
    
    def get_books_by_genre(cls, genre):
        return cls.objects.filter(genre=genre)
    
    def get_most_popular(cls):
        return cls.objects.order_by('-rating')[:10]
    
    def published_in_year(cls, year):
        return cls.objects.filter(publication_date__year=year)
    
    def count_books_by_genre(cls, genre):
        return cls.objects.filter(genre=genre).count()



