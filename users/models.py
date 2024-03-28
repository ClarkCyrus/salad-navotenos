from django.contrib.auth.models import AbstractUser
from django.db import models

class SaladUser(AbstractUser):
    profile_image = models.BinaryField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    pass
    
class Employee(SaladUser):
    position = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

class Customer(SaladUser):
    contact_number = models.CharField(max_length=20, blank=True)
    shipping_address = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

