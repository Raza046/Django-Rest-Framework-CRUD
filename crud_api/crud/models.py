from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):

    def __str__(self):
        return self.username

    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Product(models.Model):

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.Prod_Name

    Prod_Name = models.CharField(max_length=250)
    Prod_Author = models.CharField(max_length=150)
    Prod_Price = models.IntegerField()

