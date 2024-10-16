from rest_framework import serializers
from .models import BooksBookBookshelves, BooksSubject, BooksFormat, BooksBook, BooksAuthor, BooksLanguage, BooksBookLanguages, BooksBookSubjects, BooksBookshelf, BooksBookAuthors   

class BooksAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksAuthor
        fields = "__all__"


class BooksBookAuthorsSerializer(serializers.ModelSerializer):
    author = BooksAuthorSerializer()
    class Meta:
        model = BooksBookAuthors
        fields = ["author"]


class BooksLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksLanguage
        fields = "__all__"


class BooksBookLanguagesSerializer(serializers.ModelSerializer):
    language = BooksLanguageSerializer()
    class Meta:
        model = BooksBookLanguages
        fields = ["language"]


class BooksSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksSubject
        fields = "__all__"


class BooksBookSubjectsSerializer(serializers.ModelSerializer):
    subject = BooksSubjectSerializer()
    class Meta:
        model = BooksBookSubjects
        fields = ["subject"]


class BooksBookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksBookshelf
        fields = "__all__"


class BooksBookBookshelvesSerializer(serializers.ModelSerializer):
    bookshelf = BooksBookshelfSerializer()
    class Meta:
        model = BooksBookBookshelves
        fields = ["bookshelf"]


class BooksFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksFormat
        fields = ['mime_type', 'url']


class BooksBookSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()
    languages = serializers.SerializerMethodField()
    subjects = serializers.SerializerMethodField()
    bookshelves = serializers.SerializerMethodField()
    formats = BooksFormatSerializer(many=True, source='booksformat_set') 

    class Meta:
        model = BooksBook
        fields = ['gutenberg_id', 'title', 'authors', 'languages', 'subjects', "bookshelves", "formats"]

    def get_authors(self, obj):
        return BooksBookAuthorsSerializer(obj.booksbookauthors_set.all().select_related('author'), many=True).data

    def get_languages(self, obj):
        return BooksBookLanguagesSerializer(obj.booksbooklanguages_set.all().select_related('language'), many=True).data

    def get_subjects(self, obj):
        return BooksBookSubjectsSerializer(obj.booksbooksubjects_set.all().select_related('subject'), many=True).data

    def get_bookshelves(self, obj):
        return BooksBookBookshelvesSerializer(obj.booksbookbookshelves_set.all().select_related('bookshelf'), many=True).data