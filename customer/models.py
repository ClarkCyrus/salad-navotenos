from django.contrib.auth.models import AbstractUser
from django.db import models

class Customer(AbstractUser):
    contact_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username