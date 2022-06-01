from django.shortcuts import render
from Axel_app.models import *
from django.http import HttpResponse

def inicio(request):
    return render(request, "padre.html")

def lista_familiares(request):
    
    lista_familiares = Familiares.objects.all()
    datos_dicc_familiares = {"datos":lista_familiares}
    return render(request, "plantilla_familiares.html", datos_dicc_familiares)

def lista_amigos(request):
    
    lista_amigos = Amigos.objects.all()
    datos_dicc_amigos = {"datos_amigos":lista_amigos}
    return render(request, "plantilla_amigos.html", datos_dicc_amigos)

def lista_tutores(request):
    
    lista_tutores = Tutores.objects.all()
    datos_dicc_tutores = {"datos_tutores":lista_tutores}
    return render(request, "plantilla_tutores.html", datos_dicc_tutores)

def alta_familiares(request):
    if request.method == "POST":

        familiar = Familiares(request.POST['documento'], request.POST['nombre'], request.POST['fecha_de_nacimiento'])
        familiar.save()
        return render(request, "formulario_familiares.html")
    return render(request, "formulario_familiares.html")




'''
def alta_familiares(request):
    familiar = Familiares(documento="29", nombre="Axel", fecha="1992-9-24")
    familiar.save()
    familiar = Familiares(documento="34", nombre="Ivan", fecha="1986-4-2")
    familiar.save()
    familiar = Familiares(documento="66", nombre="Susana", fecha="1956-3-22")
    familiar.save()
    return render(request, "plantilla.html")
'''