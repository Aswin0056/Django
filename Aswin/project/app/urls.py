from django.contrib import admin
from django.urls import path
from .views import book_list_create_view, book_delete_view , home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home , name = 'home'),
    path('books/', book_list_create_view, name='book-list-create'),
    path('books/<int:pk>/', book_delete_view, name='book-delete'),
]


