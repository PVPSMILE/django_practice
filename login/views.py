from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str

from django.contrib.auth import logout as auth_logout

from .models import CustomUser
from .forms import RegistrationForm
from .models import CustomUser

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data['username']
            phone = cleaned_data['phone']
            email = cleaned_data['email']
            password = cleaned_data['password']

        
            user = CustomUser(
                username=username,
                phone=phone,
                email=email,
                is_admin=False,  
                password=password,
                is_email_verified=False  
            )
            user.save()  
            
            # Генерация токена и UID для дальнейшего использования
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            current_site = get_current_site(request)
            confirmation_url = reverse('activate', kwargs={'uidb64': uid, 'token': token})
            full_confirmation_url = f"http://{current_site.domain}{confirmation_url}"

            message = (
                f'Здравствуйте,\n\n'
                f'Пожалуйста, подтвердите ваш адрес электронной почты, перейдя по следующей ссылке:\n'
                f'{full_confirmation_url}\n\n'
                f'Спасибо!'
            )
            send_mail(
                subject='Подтверждение электронной почты',
                message=message,
                from_email='frank01zeroy@gmail.com',
                recipient_list=[email],
                fail_silently=False,
            )

            print(user)


            # login(request, user)
            return redirect('/login')  
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})

def activate(request, uidb64, token):
    try:
        # Декодируем UID из URL
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
   
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    # Проверяем токен
    if user is not None and default_token_generator.check_token(user, token):
        user.is_email_verified = True  
        user.save() 
        print(f'Почта подтверждена! Теперь вы можете войти.')  
        return HttpResponse("Email confirmed")
    else:
        return render(request, 'invalid_link.html')  
    
    
def login_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        
        if username and password:
            try:
        
                user = CustomUser.objects.get(username=username)
                if user.is_email_verified:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse("Email not confirmed")
            except CustomUser.DoesNotExist:
                return HttpResponse("User does not exist")

        else:
            return render(request, 'login/login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

def logout_view(request):
   
    auth_logout(request)  # Выход пользователя
    return redirect('/') 