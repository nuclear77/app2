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
    author = models.ForeignKey(Author, on_delete=models.ManyToManyRel)
    library = models.ForeignKey(Library, on_delete=models.ManyToOneRel)


class LibraryBook(models.Model):
    library = models.ForeignKey(Library, on_delete=models.ManyToOneRel)
    books = models.ManyToManyField(Book)
