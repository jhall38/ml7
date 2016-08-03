from django.forms import widgets
from rest_framework import serializers
from bookstore.models import Book, Author, Publisher

class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = ('id', 'name')
class PublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model = Publisher
		fields = ('id', 'name')

class BookSerializer(serializers.ModelSerializer):
	authors = AuthorSerializer(many=True)
	publishers = PublisherSerializer(many=True)
	class Meta:
		model = Book
		fields = ('id', 'title', 'publish_date', 'price', 'link', 'cover_image_url', 'authors', 'publishers')
