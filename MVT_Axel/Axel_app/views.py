from django.http import HttpResponse
from django.shortcuts import render
from Axel_app.models import Familiares
from django.template import loader

def familiares(request):
    
    familiares = Familiares.objects.all()
    dicc = {"familiares":familiares}
    plantilla = loader.get_template("plantilla.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)