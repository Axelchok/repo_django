from django.db import models

class Familiares(models.Model):
    documento = models.IntegerField()
    nombre = models.CharField(max_length=30)
    fecha = models.DateField()