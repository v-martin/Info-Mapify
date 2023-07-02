from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)
    population = models.IntegerField(default=0)
    description = models.TextField(max_length=1000, null=True)
    gdp = models.FloatField(default=0)
    gdp_ppp = models.FloatField(default=0)
    fertility_rate = models.FloatField(default=0)
    median_age = models.FloatField(default=0)

    class Meta:
        table = 'countries'
        ordering = ['name']

    def __str__(self):
        return self.name
