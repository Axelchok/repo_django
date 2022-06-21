from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
class Familiares_formulario(forms.Form):

    documento = forms.IntegerField()
    nombre = forms.CharField(max_length=40)
    fecha = forms.DateField()

class Tutores_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    curso = forms.CharField(max_length=40)
    comision = forms.IntegerField()

class Amigos_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    deporte_favorito = forms.CharField(max_length=40)
    edad = forms.IntegerField()

class Login(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

class UserEditForm(UserCreationForm):

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
