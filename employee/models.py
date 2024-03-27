from django.contrib.auth import get_user_model
from django.db import models

class Employee(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
