from django.http import HttpResponse
from django.template import loader 
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import book
from .serializers import BookSerializer



def library(request):
  mylibrary = book.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mylibrary': mylibrary,
  }
  return HttpResponse(template.render(context, request))


def home(request):
    return render(request ,'home.html')
    
def favourite(request):
   context = {
      'favourite_items' : ['python','django' , 'html', 'c++']
   }
   return render(request ,'favourite.html' , context )













@api_view(['GET', 'POST'])
def book_list_create_view(request):
    if request.method == 'GET':
        books = book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def book_delete_view(request, pk):
    Book = get_object_or_404(book, pk=pk)
    if request.method == 'DELETE':
        Book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)