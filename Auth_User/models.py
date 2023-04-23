from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from scipy.signal import cascade


class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
