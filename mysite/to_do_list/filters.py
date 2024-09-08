from django_filters import FilterSet
from .models import *


class BookFilter(FilterSet):
    class Meta:
        model = Book
        fields = {

            'date_created': ['gte', 'lte'],

        }