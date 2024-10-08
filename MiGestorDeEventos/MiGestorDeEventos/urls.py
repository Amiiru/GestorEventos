"""
URL configuration for MiGestorDeEventos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from eventos.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    #path("", include("eventos.urls")),
    path("",eventos),
     path('eventos/', eventos, name='evento-list'),
    path('crearEvento/', crearEventos, name='evento_form'),
    path('organizadores/', OrganizadorListView.as_view(), name='organizador-list'),
    path('organizadores/crear/', OrganizadorCreateView.as_view(), name='organizador-crear'),
    path('login/', iniciarSesion, name='login'),
    path('editar-evento/<int:id>/', editar_evento, name='editar-evento'),
    path('registrarse/',registrarse, name='registrarse'),
    path('logout/', cerrarSesion, name='logout'),
    
]
