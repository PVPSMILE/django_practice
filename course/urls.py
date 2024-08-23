from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_main, name='course'),
    path('english/', views.english_course, name='english_course'),
    path('lessons/<int:course_id>/', views.load_lessons, name='load_lessons'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    
    path('save_progress/<int:lesson_id>/', views.save_progress, name='save_progress'),
    
    path('get_assignments/<int:lesson_id>/', views.get_assignments, name='get_assignments'),
    path('load_lesson/<int:lesson_id>/', views.load_lesson, name='load_lesson'),
    path('add_lesson/', views.add_lesson, name='add_lesson'),
    path('update_lesson/', views.update_lesson, name='update_lesson'),
]
