from django.urls import path

from MiGestorDeEventos.eventos import admin
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('eventos/', views.eventos, name='listaeventos'),
    
]