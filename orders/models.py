from django.db import models
from users.models import Salad_Customer, Crochet_Customer

class Salad_Order(models.Model):
    user = models.ForeignKey(Salad_Customer, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created = models.DateField(auto_now_add=True)
    shipping_fee = models.FloatField()
    total_price = models.FloatField()
    shipping_address = models.TextField()

    def __str__(self):
        return f"Order #{self.id}: {self.status}"
    

class Crochet_Transaction(models.Model):
    user = models.ForeignKey(Crochet_Customer, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    total_price = models.FloatField()
    shipping_fee = models.FloatField()
    shipping_address = models.TextField()

    class Meta:
        abstract = True

class Crochet_Order(Crochet_Transaction):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

class Crochet_Cart(Crochet_Transaction):
    crochet_order = models.ForeignKey(Crochet_Order, related_name='cart_orders', on_delete=models.CASCADE)


