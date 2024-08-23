from django.db import models
from base.models import BaseUser

class Teacher(BaseUser):
    subject = models.CharField(max_length=50)
    known_skills = models.TextField(blank=True)
    courses = models.ManyToManyField('course.Course', related_name='teachers')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"