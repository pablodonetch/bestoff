from django.urls import path
from .views import *

urlpatterns =[
    path('login/', acceso_login, name="acceso_login"),
]