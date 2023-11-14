from django.contrib import admin
from .models import Author, Library, LibraryBook, Book


class CustomAd(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('name', 'address')


class CustomA(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('first_mane', 'last_name')


class CustomAdm(admin.ModelAdmin):
    search_fields = ('title',)


class CustomAdmi(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'year', 'author', 'library')


admin.site.register(Author, CustomA)
admin.site.register(Library, CustomAd)
admin.site.register(LibraryBook, CustomAdm)
admin.site.register(Book, CustomAdmi)

