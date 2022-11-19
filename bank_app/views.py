from django.db.migrations import serializer
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from bank_app.filters import CustomerFilter
from bank_app.models import Customer
from bank_app.serializers import CustomerSerializer


class CustomerViewList(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_class = CustomerFilter
    search_fields = ['first_name', 'last_name', 'address']
    ordering_fields = ['first_name', 'last_name']
    ordering = ['first_name']

