from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

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
    path("borrar_tutor/<int:id>", views.borrar_tutor, name='borrar_tutor'),
    path("editar_perfil", views.editar_perfil, name='editar_perfil'),
    path("editar_familiar/<int:id>", views.editar_familiar, name='editar_familiar'),
    path("editar_familiar", views.editar_familiar, name='editar_familiar'),
    path("editar_amigo/<int:id>", views.editar_amigo, name='editar_amigo'),
    path("editar_amigo", views.editar_amigo, name='editar_amigo'),
    path("editar_tutor/<int:id>", views.editar_tutor, name='editar_tutor'),
    path("editar_tutor", views.editar_tutor, name='editar_tutor'),
    path("login", views.login_request, name='login'),
    path("register", views.register, name='register'),
    path("logout", LogoutView.as_view(template_name="logout.html"), name='logout'),
    path("editar_perfil", views.editar_perfil, name='editar_perfil'),
    # path("agregar_avatar", views.agregar_avatar, nam='agregar_avatar')
]
