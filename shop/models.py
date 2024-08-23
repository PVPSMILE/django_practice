from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=40)
    amount = models.IntegerField(default=0)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return self.name