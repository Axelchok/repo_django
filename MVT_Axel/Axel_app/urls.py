from django.urls import path
from . import views

urlpatterns = [
    path("familiares/", views.Familiares)
]