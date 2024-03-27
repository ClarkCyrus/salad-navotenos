from django.db import models
from main.models import SaladUser

class Employee(SaladUser):
    position = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
