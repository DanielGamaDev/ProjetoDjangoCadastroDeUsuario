
from django.urls import path
from app_cadastro_usuario import views

urlpatterns = [
    # rota, view responsavel, nome de referência
    path('', views.home, name='home'),
]
