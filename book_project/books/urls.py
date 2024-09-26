from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_books,name='view_books'),
]