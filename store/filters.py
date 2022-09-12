from cgitb import lookup
from dataclasses import fields
from pyexpat import model
import django_filters
from django_filters import CharFilter,DateFilter
from .models import Product


class Product_filter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name']
