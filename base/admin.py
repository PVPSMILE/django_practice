# course/admin.py
from django.contrib import admin
from course.models import Course, Lesson, Sentence, UserProgress
from login.models import CustomUser  # Импортируйте модель CustomUser

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name',)
    search_fields = ('course_name',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('course', 'title', 'lesson_number')
    list_filter = ('course',)
    search_fields = ('title', 'lesson_number')
    autocomplete_fields = ['course']

@admin.register(Sentence)
class SentenceAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'correct_sentence', 'sentence', 'assignment_id', 'is_correct')
    list_filter = ('lesson', 'is_correct')
    search_fields = ('correct_sentence', 'sentence', 'assignment_id')
    autocomplete_fields = ['lesson']

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'completed')
    list_filter = ('completed', 'lesson', 'user')
    search_fields = ('user__username', 'lesson__title')
    autocomplete_fields = ['user', 'lesson']
