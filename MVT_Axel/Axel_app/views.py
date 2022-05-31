from django.shortcuts import render
from Axel_app.models import Familiares
from django.http import HttpResponse

def inicio(request):
    return render(request, "index.html")

def lista_familiares(request):
    
    lista_familiares = Familiares.objects.all()
    datos_dicc = {"datos":lista_familiares}
    return render(request, "plantilla.html", datos_dicc)

def alta_familiares(request):
    familiar = Familiares(documento="29", nombre="Axel", fecha="1992-9-24")
    familiar.save()
    familiar = Familiares(documento="34", nombre="Ivan", fecha="1986-4-2")
    familiar.save()
    familiar = Familiares(documento="66", nombre="Susana", fecha="1956-3-22")
    familiar.save()
    return render(request, "plantilla.html")