from django.db import models

# Create your models here.
from django.urls import reverse


class Wine(models.Model):
    """Model representing a wine """

    country = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the wine')
    designation = models.CharField(max_length=200)
    points = models.IntegerField(blank=False, null=False, default=0)
    price = models.FloatField(blank=True, null=True)
    province = models.CharField(max_length=200)
    region_1 = models.CharField(max_length=200)
    region_2 = models.CharField(max_length=200)
    variety = models.CharField(max_length=200, verbose_name='Grape Variety')
    winery = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return self.designation + ' ' +self.winery + ' wine'

    def display_price(self):
        """Create a string for the price. This is required to display price in Admin."""
        return '$ '+str(self.price)

    display_price.short_description = 'Price'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this wine."""
        return reverse('wine-detail', args=[str(self.id)])

    def as_dict(self):
        return {
            'id': self.id,
            'country': self.country,
            'description': self.description,
            'designation': self.designation,
            'points': self.points,
            'price': self.price,
            'province': self.province,
            'region_1': self.region_1,
            'region_2': self.region_2,
            'variety': self.variety,
            'winery': self.winery,
        }
