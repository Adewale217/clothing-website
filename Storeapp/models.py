from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username
