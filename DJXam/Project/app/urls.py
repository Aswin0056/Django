from django.contrib import admin
from django.urls import path
from .views import home , library , favourite , book_list_create_view , book_delete_view

urlpatterns = [
    path('/admin', admin.site.urls),
    path('library/',library ,name = "library"),
    path('',home , name = "home"),
    path('favourite',favourite , name = "favourite"),
    path('books/', book_list_create_view, name='book-list-create'),
    path('books/<int:pk>/', book_delete_view, name='book-delete'),
]