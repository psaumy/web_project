from django.contrib import admin

# Register your models here.
from .models import Wine


class WineAdmin(admin.ModelAdmin):
    list_display = ('winery', 'variety', 'designation', 'country', 'points', 'display_price')

    list_filter = ('country', 'points')

admin.site.register(Wine, WineAdmin)