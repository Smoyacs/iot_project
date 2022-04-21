from django import forms
from django.contrib.auth import get_user_model

# extendemos la clase UserCreationForm y UserChangeForm para que nos permita crear un formulario de registro y de edición de usuarios customizados
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# Create yours form here.


# Se toma en cuenta que la contraseña viene de forma implicita dentro de los campos de texto, por lo que no es necesario definir un campo de contraseña en el formulario de edición de usuarios.

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('username','email', 'password1', 'password2')
        
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')