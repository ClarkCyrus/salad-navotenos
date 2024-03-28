from django.db import models

class Salad(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    # Add other fields as needed

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('salad_detail', args=[str(self.id)])