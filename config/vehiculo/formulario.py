from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(
        required=True,
        min_length=4, 
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',  # Clase personalizada para field grandes
            'id': 'username',
            'placeholder': 'Username'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg',  # Clase personalizada
            'id': 'email',
            'placeholder': 'example@gmail.com'
        })
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg',  # Clase personalizada
            'id': 'password',
            'placeholder': 'Password'
        })
    )
    
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya se encuentra en uso')

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya se encuentra en uso')

        return email