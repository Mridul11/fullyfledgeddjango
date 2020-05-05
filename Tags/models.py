from django.db import models
from products.models import Product

class Tag(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.title 
