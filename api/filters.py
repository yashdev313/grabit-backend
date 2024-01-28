from django_filters import rest_framework as filters
from .models import ProductModel,ColorVariantModel

class CustomFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='price',lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price',lookup_expr='lte')
    color = filters.CharFilter(field_name='colors__name',lookup_expr='iexact')
    size = filters.CharFilter(field_name='sizes__name',lookup_expr='iexact')
    # size = filters.CharFilter(field_name='size_variants__size',lookup_expr='iexact')
    category = filters.CharFilter(field_name='category__name', lookup_expr='iexact')



    class Meta:
        model=ProductModel
        fields=['name']

