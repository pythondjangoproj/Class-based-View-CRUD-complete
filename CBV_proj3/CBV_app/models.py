from django.db import models
from django.urls import reverse
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    ceo = models.CharField(max_length=30)

    def __repr__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('CBV_app:detail', args=[self.pk,])
