from django.db import models
from base.models import BaseUser

class Student(BaseUser):
    grade = models.CharField(max_length=10)
    teacher = models.ForeignKey('teacher.Teacher', on_delete=models.CASCADE, related_name='students')
    parent = models.ForeignKey('parent.Parent', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    courses = models.ManyToManyField('course.Course', related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.grade}"