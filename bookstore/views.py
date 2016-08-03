from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bookstore.models import Book, Author, Publisher
from bookstore.serializers import BookSerializer, AuthorSerializer, PublisherSerializer

@api_view(['GET', 'POST'])
def book_list(request, format=None):
	if request.method == 'GET':
		books = Book.objects.all()
		serializer = BookSerializer(books, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = BookSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def book_detail(request, pk, format=None):
	try:
		books = Book.objects.get(pk=pk)
	except Book.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = BookSerializer(books)
		return Response(serializer.data)
