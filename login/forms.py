from django import forms
from login.models import CustomUser

from django import forms
from login.models import CustomUser



class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput, max_length=100, required=True)

    def clean_username(self):
        username = self.cleaned_data.get('username')

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        return phone

    
# class RegistrationForm(forms.Form):
    # username = forms.CharField(max_length=30, required=True)
    # phone = forms.CharField(max_length=100, required=True)
    # password = forms.CharField(widget=forms.PasswordInput, max_length=100, required=True)
    # confirmations = forms.BooleanField(widget=forms.RadioSelect(attrs={'class': 'form-control:'}))
    # email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control:'}))

    # class Meta:
    #     model = CustomUser
    #     fields = [
    #         'username',
    #         'email',
    #         'phone',
    #         'password',
    #     ]

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
        # if CustomUser.objects.filter(username=username).exists():
        #     raise forms.ValidationError('Username already exists')
        # return username
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
        # if CustomUser.objects.filter(email=email).exists():
        #     raise forms.ValidationError('Email already exists')
        # return email
    # def clean_phone(self):
    #     phone = self.cleaned_data.get('phone')
        # if len(phone) != 10:
        #     raise forms.ValidationError('Invalid phone number')
        # if CustomUser.objects.filter(phone=phone).exists():
        #     raise forms.ValidationError('Phone already exists')
        # return phone
