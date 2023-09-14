from .models import Sales, Customer
import django_filters


class CustomerFilter(django_filters.FilterSet):
    Customer_Name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Customer
        fields = ['id', 'Customer_Name', 'Customer_Code', 'City', 'State', 'gstin', 'Address']
