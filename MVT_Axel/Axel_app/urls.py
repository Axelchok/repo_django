from django.urls import path
from . import views

urlpatterns = [
    path("lista_familiares", views.lista_familiares, name='familiares'),
    path("lista_amigos", views.lista_amigos, name='amigos'),
    path("lista_tutores", views.lista_tutores, name='tutores'),
    path("alta_familiares", views.alta_familiares, name='alta_familiares'),
    path("alta_tutores", views.alta_tutores, name='alta_tutores'),
    path("alta_amigos", views.alta_amigos, name='alta_amigos'),
    path("buscar_familiar", views.buscar_familiar, name='buscar_familiar')
]
