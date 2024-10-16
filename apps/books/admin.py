from django.contrib import admin
from .models import (
    BooksAuthor,
    BooksBook,
    BooksBookAuthors,
    BooksBookBookshelves,
    BooksBookLanguages,
    BooksBookSubjects,
    BooksBookshelf,
    BooksFormat,
    BooksLanguage,
    BooksSubject
)

# Register your models here.

@admin.register(BooksAuthor)
class BooksAuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_year', 'death_year')
    search_fields = ('name',)

@admin.register(BooksBook)
class BooksBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'gutenberg_id', 'media_type', 'download_count')
    search_fields = ('title', 'gutenberg_id')
    list_filter = ('media_type',)

@admin.register(BooksBookAuthors)
class BooksBookAuthorsAdmin(admin.ModelAdmin):
    list_display = ('book', 'author')
    autocomplete_fields = ['book', 'author']

@admin.register(BooksBookBookshelves)
class BooksBookBookshelvesAdmin(admin.ModelAdmin):
    list_display = ('book', 'bookshelf')
    autocomplete_fields = ['book', 'bookshelf']

@admin.register(BooksBookLanguages)
class BooksBookLanguagesAdmin(admin.ModelAdmin):
    list_display = ('book', 'language')
    autocomplete_fields = ['book', 'language']

@admin.register(BooksBookSubjects)
class BooksBookSubjectsAdmin(admin.ModelAdmin):
    list_display = ('book', 'subject')
    autocomplete_fields = ['book', 'subject']

@admin.register(BooksBookshelf)
class BooksBookshelfAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(BooksFormat)
class BooksFormatAdmin(admin.ModelAdmin):
    list_display = ('book', 'mime_type', 'url')
    list_filter = ('mime_type',)
    autocomplete_fields = ['book']

@admin.register(BooksLanguage)
class BooksLanguageAdmin(admin.ModelAdmin):
    list_display = ('code',)
    search_fields = ('code',)

@admin.register(BooksSubject)
class BooksSubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
