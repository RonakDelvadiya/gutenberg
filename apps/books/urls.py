from django.urls import path
from .views import BooksBookList

urlpatterns = [
    path('book-list/', BooksBookList.as_view(), name='book-list'),
]
