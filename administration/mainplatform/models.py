from django.db import models
from login.models import User
import datetime

# Create your models here.
MAX_LENGTH_UNIT: int = 3
MAX_LENGTH_PRODUCT_DESCRIPTION = 150



class Products(models.Model):
    unit: str = models.CharField(max_length=MAX_LENGTH_UNIT)
    description: str = models.CharField(max_length=MAX_LENGTH_PRODUCT_DESCRIPTION)
    amount: int = models.IntegerField()


class Request(models.Model):
    product: Products = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    user_aux: User = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_aux_request')
    user_don: User = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_don_request', null=True)
    date_created: datetime = models.DateTimeField(auto_now_add=True)
    date_accepted: datetime = models.DateTimeField(auto_now_add=True)

