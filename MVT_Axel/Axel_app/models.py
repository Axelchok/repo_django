from django.db import models

class Familiares(models.Model):
    documento = models.IntegerField()
    nombre = models.CharField(max_length=30)
    fecha = models.DateField()

class Amigos(models.Model):
    nombre = models.CharField(max_length=30)
    deporte_favorito = models.CharField(max_length=30)
    edad = models.IntegerField()

class Tutores(models.Model):
    nombre = models.CharField(max_length=30)
    curso = models.CharField(max_length=30)
    comision = models.CharField(max_length=30)
