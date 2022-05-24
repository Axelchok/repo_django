from django.shortcuts import render
from Axel_app.models import Familiares
from django.http import HttpResponse

def inicio(request):
    return render(request, "index.html")

def lista_familiares(request):
    
    lista_familiares = Familiares.objects.all()
    datos = {"datos":lista_familiares}
    return render(request, "plantilla.html", datos)

def alta_familiares(request):
    familiar = Familiares(nombre="Axel", edad="29", nacimiento="1992-9-24")
    familiar.save()
    familiar = Familiares(nombre="Ivan", edad="34", nacimiento="1986-4-2")
    familiar.save()
    familiar = Familiares(nombre="Susana", edad="66", nacimiento="1956-3-22")
    familiar.save()
    
    return HttpResponse("Todo Ok")