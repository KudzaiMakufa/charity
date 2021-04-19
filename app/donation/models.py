from django.db import models
from listrequests.models import Charity_Request


class Donation(models.Model):
  

    name = models.ForeignKey(Charity_Request, on_delete=models.CASCADE,default=None)
    purpose = models.CharField(blank=True , default='' ,max_length=200)
    beneficiaries = models.CharField(blank=True , default='' ,max_length=200)
    donation_details = models.CharField(blank=True , default='' ,max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    created_at = models.DateField(default=None)
    updated_at = models.DateField(default=None)
    created_by = models.IntegerField(default=None)


