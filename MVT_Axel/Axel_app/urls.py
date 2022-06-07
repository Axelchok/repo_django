from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path("lista_familiares", views.lista_familiares, name='familiares'),
    path("lista_amigos", views.lista_amigos, name='amigos'),
    path("lista_tutores", views.lista_tutores, name='tutores'),
    path("alta_familiares", views.alta_familiares, name='alta_familiares'),
    path("alta_tutores", views.alta_tutores, name='alta_tutores'),
    path("alta_amigos", views.alta_amigos, name='alta_amigos'),
    path("buscar_familiar", views.buscar_familiar, name='buscar_familiar'),
    path("buscar_amigo", views.buscar_amigo, name='buscar_amigo'),
    path("buscar_tutor", views.buscar_tutor, name='buscar_tutor'),
    path("borrar_familiar/<int:id>", views.borrar_familiar, name='borrar_familiar'),
    path("borrar_amigo/<int:id>", views.borrar_amigo, name='borrar_amigo'),
    path("borrar_tutor/<int:id>", views.borrar_tutor, name='borrar_tutor')
]
