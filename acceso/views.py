from email.mime import image
from unittest import result
from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
from django.contrib import messages
from core.models import *
from bestoff.forms import *
from .forms import *
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from datetime import datetime, date, timedelta
from funcionespy import *
import time
from django.conf import settings
from django.contrib.auth.hashers import make_password

def acceso_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    form = Formulario_Login(request.POST or None)
    if request.method =='POST':
        if form.is_valid():
            correo = request.POST['correo']
            password = request.POST['password']
            user = authenticate(request, username=correo, password=password)
            if user is not None:
                login(request, user)
                usersMetadata = UsersMetadata.objects.filter(user_id=request.user.id).get()
                request.session['users_metadata_id'] =  usersMetadata.id
                return HttpResponseRedirect('/')
            else:
                messages.add_message(request, messages.WARNING, f'Los datos ingresados no son correctos, por favor vuelva a intentar.')
                return HttpResponseRedirect('/acceso/login')
    return render(request, 'acceso/login.html', {'form': form})


def acceso_salir(request):
    logout(request)
    try:
        del request.session['users_metadata_id']
    except KeyError:
        pass
    messages.add_message(request, messages.WARNING, f'Se cerró la sesión exitosamente.')
    return HttpResponseRedirect('/')
