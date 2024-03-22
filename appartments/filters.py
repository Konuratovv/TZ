from django_filters import rest_framework as filters
from .models import Appartments

class AppartmentFilter(filters.FilterSet):
    status = filters.CharFilter(field_name='status', lookup_expr='iexact')

    class Meta:
        model = Appartments
        fields = ['status']