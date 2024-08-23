from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponse
from .models import Student
from django.contrib.auth import get_user_model
from .forms import StudentLoginForm

def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                # Искать пользователя по first_name (или last_name, если нужно)
                student = Student.objects.get(first_name=username)
                # Выполнить авторизацию пользователя
                login(request, student, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('home')  # укажите нужный URL
            except Student.DoesNotExist:
                return HttpResponse("Пользователь с таким именем не найден.")
    else:
        form = StudentLoginForm()
    return render(request, 'login.html', {'form': form})
