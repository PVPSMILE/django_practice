from django.urls import path
from login import views

urlpatterns = [
    path('login/', views.login_in, name='login'),
    path('reg/', views.register, name='register'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'), 
    path('logout/', views.logout_view, name='logout')
]
