from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio),
    path("lista_familiares", views.lista_familiares, name='familiares'),
    path("lista_amigos/", views.lista_amigos, name='amigos'),
    path("lista_tutores/", views.lista_tutores, name='tutores'),
    path("alta_familiares/", views.alta_familiares, name='alta_familiares'),
]
