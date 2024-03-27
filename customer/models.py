from main.models import SaladUser
from django.db import models

class Customer(SaladUser):
    contact_number = models.CharField(max_length=20, blank=True)
    
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


