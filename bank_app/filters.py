from django_filters.rest_framework import FilterSet

from bank_app.models import Customer


class CustomerFilter(FilterSet):
    class Meta:
        model = Customer
        fields = {
            'first_name': ['exact'],
            'last_name': ['exact'],
            'email': ['exact'],
            'address': ['exact', 'contains'],
        }