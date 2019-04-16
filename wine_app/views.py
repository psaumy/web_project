from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django_filters.views import FilterView
from django_tables2 import SingleTableView, RequestConfig, SingleTableMixin

from wine_app.filters import WineFilter
from wine_app.forms import WineListFormHelper
from wine_app.models import Wine

from wine_app.tables import WineTable
from wine_app.utils import PagedFilteredTableView

@login_required
def index(request):
    """View function for home page of site."""


    context = {
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class WineDetailView(LoginRequiredMixin, generic.DetailView):
    model = Wine


class WineListView(LoginRequiredMixin, PagedFilteredTableView):
    model = Wine
    template_name = 'wine_app/wine_list.html'
    context_object_name = 'wine'
    ordering = ['country']
    table_class = WineTable
    filter_class = WineFilter
    formhelper_class = WineListFormHelper

    def get_queryset(self):
        qs = super(WineListView, self).get_queryset()
        return qs

    def post(self, request, *args, **kwargs):
        return PagedFilteredTableView.as_view()(request)

    def get_context_data(self, **kwargs):
        context = super(WineListView, self).get_context_data(**kwargs)
        context['nav_table'] = True
        search_query = self.get_queryset()
        table = WineTable(search_query)
        RequestConfig(self.request, paginate={'per_page': 15}).configure(table)
        context['table'] = table
        return context


def get_wine(request, pk):
    wine = Wine.objects.filter(id=pk)
    wine = [ obj.as_dict() for obj in wine ][0]
    return HttpResponse(json.dumps(wine),
                        status=200,
                        content_type='application/json')

@login_required
def portfolio(request):
    """View function for portfolio page of site."""
    context = {
    }
    # Render the HTML template portfolio.html with the data in the context variable
    return render(request, 'portfolio.html', context=context)


@login_required
def restapi(request):
    """View function for portfolio page of site."""
    context = {
    }
    # Render the HTML template portfolio.html with the data in the context variable
    return render(request, 'restapi.html', context=context)