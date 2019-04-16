import django_tables2 as tables
from django_tables2 import A

from .models import Wine

class WineTable(tables.Table):
    id = tables.LinkColumn('wine-detail', args=[A('pk')])

    class Meta:
        model = Wine
        template_name = 'django_tables2/bootstrap.html'



        fields = ('id', 'winery', 'variety', 'designation', 'country', 'points', 'display_price')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There are no wined matching the search criteria..."


# class CustomerTable(tables.Table):
#     account_number = tables.LinkColumn('customer-detail', args=[A('pk')])
#     customer_first_name = tables.LinkColumn('customer-detail', args=[A('pk')])
#     customer_last_name = tables.LinkColumn('customer-detail', args=[A('pk')])
#     customer_email = tables.LinkColumn('customer-detail', args=[A('pk')])
#
#     class Meta:
#         model = Customer
#         fields = ('account_number', 'customer_first_name',
#                   'customer_last_name', 'primary_phone', 'city',
#                   'state', 'customer_email')
#         attrs = {"class": "table-striped table-bordered"}
#         empty_text = "There are no wined matching the search criteria..."