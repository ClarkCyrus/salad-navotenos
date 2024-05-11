from django.contrib.auth.models import AbstractUser
from django.db import models

class SaladUser(AbstractUser):
    profile_image = models.BinaryField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    pass
    
class Salad_Employee(SaladUser):
    position = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Salad Employee'
        verbose_name_plural = 'Salad Employees'

class Salad_Customer(SaladUser):
    contact_number = models.CharField(max_length=20, blank=True)
    shipping_address = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Salad Customer'
        verbose_name_plural = 'Salad Customers'

class Crochet_Employee(SaladUser):
    position = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Crochet Employee'
        verbose_name_plural = 'Crochet Employees'

class Crochet_Customer(SaladUser):
    contact_number = models.CharField(max_length=20, blank=True)
    shipping_address = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Crochet Customer'
        verbose_name_plural = 'Crochet Customers'

