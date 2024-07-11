"""Psy_C URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from FrontEnd.views import IndexViews
from FrontEnd.views import infoPagina
from FrontEnd.views import losProblemas
from FrontEnd.views import inicioSesion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', IndexViews, name='index'),
    path('info/', infoPagina, name='info_pagina'),
    path('problemas/', losProblemas, name='los_problemas'),
    path('login/', inicioSesion, name='inicio_sesion'),
    path('', infoPagina, name='home'),  # Definimos infoPagina como la página de inicio

]
