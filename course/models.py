# course/models.py
from django.db import models
from login.models import CustomUser

class Course(models.Model):
    course_name = models.CharField(max_length=55)

    def __str__(self):
        return self.course_name

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    lesson_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.lesson_number} - {self.title}"

class Sentence(models.Model):
    
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='sentences')
    correct_sentence = models.CharField(max_length=255)
    sentence = models.CharField(max_length=255)
    assignment_id = models.PositiveIntegerField(null=False)
    is_correct = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_sentences', null=True, blank=True)

    def __str__(self):
        return f"Sentence in {self.lesson}:"

class UserProgress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='progress')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='user_progress')
    sentences = models.ManyToManyField(Sentence, related_name='user_progress_sentences')
    completed = models.BooleanField(default=False)

    def __str__(self):  
        return f"Progress for {self.user.username}: {self.lesson.title}"