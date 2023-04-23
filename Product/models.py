from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="static/dynamicImg")
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return f"{self.product}"