from django.db import models
from django import forms
from django.forms import ModelForm, PasswordInput



class Formulario_Login(forms.Form):
    correo = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'w-full rounded-md mx-0 border-2 border-orange-200 py-4 px-2', 'placeholder': 'E-Mail', 'autocomplete':'off'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'w-full rounded-md mx-0 border-2 border-orange-200 py-4 px-2', 'placeholder': 'Contraseña', 'autocomplete':'off'}))