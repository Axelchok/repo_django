from django.shortcuts import render, redirect
from Axel_app.models import *
from django.http import HttpResponse
from Axel_app.forms import *

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
        
        mi_formulario = Familiares_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            familiar = Familiares(documento=request.POST['documento'], nombre=request.POST['nombre'], fecha=request.POST['fecha'])
            familiar.save()
            return render(request, "formulario_familiares.html")
        
    return render(request, "formulario_familiares.html")

def alta_tutores(request):
    if request.method == "POST":
        
    
        mi_formulario_turores = Tutores_formulario(request.POST)
        
        if mi_formulario_amigos.is_valid():
            datos_tutores = mi_formulario_amigos.cleaned_data
        
            tutor = Tutores(nombre=request.POST.get('nombre', False), curso=request.POST.get('curso', False), comision=request.POST.get('comision', False))
            tutor.save()
        
    return render(request, "formulario_tutores.html")

def alta_amigos(request):
    if request.method == "POST":
        
        mi_formulario_amigos = Amigos_formulario(request.POST)

        if mi_formulario_amigos.is_valid():
            datos_amigos = mi_formulario_amigos.cleaned_data

            amigo = Amigos(nombre=request.POST.get('nombre', False), deporte_favorito=request.POST.get('deporte_favorito', False), edad=request.POST.get('edad', False))
            amigo.save()
            return render(request, "formulario_amigos.html")
        
    return render(request, "formulario_amigos.html")


def buscar_familiar(request):

    if request.POST.get('nombre', False):
        nombre = request.POST.get('nombre', False)
        familiares = Familiares.objects.filter(nombre__icontains = nombre)
        return render(request, "resultado_familiares.html", {'familiares':familiares})
    return render(request, "buscar_familiar.html")





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