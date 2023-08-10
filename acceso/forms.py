from django.db import models
from django import forms
from django.forms import ModelForm, PasswordInput



class Formulario_Login(forms.Form):
    correo = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'rounded-md focus:border-orange-500', 'placeholder': 'E-Mail', 'autocomplete':'off'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'rounded-md focus:border-orange-500 ', 'placeholder': 'Contraseña', 'autocomplete':'off'}))