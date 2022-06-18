from django.db import models
from django.contrib.auth.models import User

class Familiares(models.Model):
    documento = models.IntegerField()
    nombre = models.CharField(max_length=30)
    fecha = models.DateField()
    def __str__(self):
        return f"Documento: {self.documento}. Nombre: {self.nombre}. Fecha: {self.fecha}"

class Amigos(models.Model):
    nombre = models.CharField(max_length=30)
    deporte_favorito = models.CharField(max_length=30)
    edad = models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre}. Deporte favorito: {self.deporte_favorito}. Edad: {self.edad}"

class Tutores(models.Model):
    nombre = models.CharField(max_length=30)
    curso = models.CharField(max_length=30)
    comision = models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre}. Curso: {self.curso}. Comision: {self.comision}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)