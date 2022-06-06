from django import forms

class Familiares_formulario(forms.Form):

    documento = forms.IntegerField()
    nombre = forms.CharField(max_length=40)
    fecha = forms.DateField()

class Tutores_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    curso = forms.CharField(max_length=40)
    comision = forms.IntegerField

class Amigos_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    deporte_favorito = forms.CharField(max_length=40)
    edad = forms.IntegerField