from rest_framework import generics
from .models import BooksBook
from .serializers import BooksBookSerializer
from django.db.models import Q
from django_filters import rest_framework as filters
import time


class BooksBookFilter(filters.FilterSet):
    """
    FilterSet for BooksBook model.
    
    Provides filtering options for various fields of the BooksBook model,
    including language, author, mime type, and topic.
    """
    language = filters.CharFilter(label="Language Exact", field_name='booksbooklanguages__language__code', lookup_expr='exact')
    languages = filters.CharFilter(label="Languages with comma separated", field_name='booksbooklanguages__language__code', lookup_expr='in')
    author = filters.CharFilter(label="Author with icontains", field_name='booksbookauthors__author__name', lookup_expr='icontains')
    mime_type = filters.CharFilter(label="Mime Type with icontains", field_name='booksformat__mime_type', lookup_expr='icontains')
    topic = filters.CharFilter(label="Topic (subject or bookshelf)", method='filter_topic')
    
    class Meta:
        model = BooksBook
        fields = {
            'gutenberg_id': ['exact'],
            'title': ['icontains'],
        }

    def filter_topic(self, queryset, name, value):
        """
        Custom filter method for topic field.
        
        Filters books based on subject or bookshelf names containing the given topics.
        Multiple topics can be provided as comma-separated values.
        
        Args:
            queryset (QuerySet): The initial queryset to filter.
            name (str): The name of the filter field (unused in this method).
            value (str): Comma-separated list of topics to filter by.
        
        Returns:
            QuerySet: Filtered queryset of books matching the given topics.
        """
        topics = [topic.strip() for topic in value.split(',')]
        topic_query = Q()
        for topic in topics:
            topic_query |= Q(booksbooksubjects__subject__name__icontains=topic) | Q(booksbookbookshelves__bookshelf__name__icontains=topic)
        return queryset.filter(topic_query).distinct()


class BooksBookList(generics.ListAPIView):
    """
    API view for listing BooksBook objects.
    
    Provides a paginated list of books, ordered by download count in descending order.
    Supports filtering using the BooksBookFilter.
    """
    queryset = BooksBook.objects.all().order_by('-download_count')
    serializer_class = BooksBookSerializer
    filterset_class = BooksBookFilter
