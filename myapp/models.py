from django.db import models


# Create your models here.
from django.urls import reverse


class Kite(models.Model):
    kite_name = models.CharField(max_length=25)
    kite_category = models.CharField(max_length=25)

    def __str__(self):
        return self.kite_name

    def get_absolute_url(self):
        return reverse("myapp:detail", kwargs={'pk': self.pk})


class Kite_Details(models.Model):
    available_quantity = models.PositiveIntegerField()
    available_colors = models.CharField(max_length=100)
    kite = models.ForeignKey(Kite, models.CASCADE, related_name='kites')

    def __str__(self):
        return self.kite.kite_category
