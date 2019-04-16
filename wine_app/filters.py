import django_filters

from wine_app.models import Wine


class WineFilter(django_filters.FilterSet):
    class Meta:
        model = Wine
        fields = {
            'variety': ['icontains', ],
            'country': ['icontains', ],
            'province': ['icontains', ],
            'region_1': ['icontains', ],
            'region_2': ['icontains', ],
        }
        order_by = ['country']

