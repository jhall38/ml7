from django.db import models

class Author(models.Model):
	name = models.CharField(max_length=100)

class Publisher(models.Model):
	name = models.CharField(max_length=100)

class Book(models.Model):
	title = models.CharField(max_length=100)
	publish_date = models.DateTimeField()
	summary = models.CharField(max_length=1000)
	price = models.FloatField()
	link = models.CharField(max_length=1000)
	cover_image_url = models.CharField(max_length=1000)
	authors = models.ManyToManyField('Author')
	publishers = models.ManyToManyField('Publisher')
#class Book_Author(models.Model):
#	book = models.ForeignKey(Book)
#	author = models.ForeignKey('Author')
#class Book_Publisher(models.Model):
#	book = models.ForeignKey('Book')
#	publisher = models.ForeignKey('Publisher')
