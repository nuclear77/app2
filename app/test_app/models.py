from django.db import models


class Library(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class Author(models.Model):
    first_mane = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)


class LibraryBook(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
