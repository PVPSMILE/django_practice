from django.db import models
from base.models import BaseUser

class Parent(BaseUser):
    phone_number = models.CharField(max_length=15, blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"