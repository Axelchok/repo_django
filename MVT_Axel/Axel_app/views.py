from django.shortcuts import render, redirect
from Axel_app.models import *
from django.http import HttpResponse
from Axel_app.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, "padre.html")
    

@login_required
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
        
    
        mi_formulario_tutores = Tutores_formulario(request.POST)
        
        if mi_formulario_tutores.is_valid():
            datos_tutores = mi_formulario_tutores.cleaned_data
        
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

def buscar_amigo(request):

    if request.POST.get('nombre', False):
        nombre = request.POST.get('nombre', False)
        amigos = Amigos.objects.filter(nombre__icontains = nombre)
        return render(request, "resultado_amigos.html", {'amigos':amigos})
    return render(request, "buscar_amigo.html")

def buscar_tutor(request):

    if request.POST.get('nombre', False):
        nombre = request.POST.get('nombre', False)
        tutores = Tutores.objects.filter(nombre__icontains = nombre)
        return render(request, "resultado_tutores.html", {'tutores':tutores})
    return render(request, "buscar_tutor.html")

def borrar_familiar(request, id):

    familiar = Familiares.objects.get(id=id)
    familiar.delete()
    
    familiar = Familiares.objects.all()
    return render(request, "plantilla_familiares.html")

def borrar_amigo(request, id):

    amigo = Amigos.objects.get(id=id)
    amigo.delete()
    
    amigo = Amigos.objects.all()
    return render(request, "plantilla_amigos.html")

def borrar_tutor(request, id):

    tutor = Tutores.objects.get(id=id)
    tutor.delete()
    
    tutor = Tutores.objects.all()
    return render(request, "plantilla_tutores.html")

def editar_familiar(request, id):

    familiar = Familiares.objects.get(id=id)
    
    if request.method == "POST":
        
        mi_formulario = Familiares_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            familiar.documento = datos['documento']
            familiar.nombre = datos['nombre']
            familiar.fecha = datos['fecha']
            familiar.save()
    else:
        mi_formulario = Familiares_formulario(initial={'documento':familiar.documento, 'nombre':familiar.nombre,'fecha':familiar.fecha})
    return render(request, "editar_familiar.html", {"mi_formulario":mi_formulario, "familiar":familiar})

def editar_amigo(request, id):

    amigo = Amigos.objects.get(id=id)
    
    if request.method == "POST":
        
        mi_formulario_amigos = Amigos_formulario(request.POST)

        if mi_formulario_amigos.is_valid():
            datos_amigos = mi_formulario_amigos.cleaned_data
            amigo.nombre = datos_amigos['nombre']
            amigo.deporte_favorito = datos_amigos['deporte_favorito']
            amigo.edad = datos_amigos['edad']
            amigo.save()

    else:
        mi_formulario_amigos = Amigos_formulario(initial={'nombre':amigo.nombre, 'deporte_favorito':amigo.deporte_favorito,'edad':amigo.edad})
    return render(request, "editar_amigo.html", {"mi_formulario_amigos":mi_formulario_amigos, "amigo":amigo})

def editar_tutor(request, id):

    tutor = Tutores.objects.get(id=id)
    
    if request.method == "POST":
        
        mi_formulario_tutores = Tutores_formulario(request.POST)

        if mi_formulario_tutores.is_valid():
            datos = mi_formulario_tutores.cleaned_data
            tutor.nombre = datos['nombre']
            tutor.curso = datos['curso']
            tutor.comision = datos['comision']
            tutor.save()
    else:
        mi_formulario_tutores = Tutores_formulario(initial={'nombre':tutor.nombre, 'curso':tutor.curso, 'comision':tutor.comision})
    return render(request, "editar_tutor.html", {"mi_formulario_tutores":mi_formulario_tutores, "tutor":tutor})

def login_request(request):

    if request.method == "POST":

        mi_formulario = Avatar(request.POST, request.FILES)
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                avatares = Avatar.objects.filter(user=request.user.id)
                if avatares == True:
                    return render(request, "padre.html",{"url":avatares[0].imagen.url}) 
                else:
                    default = '/static/Axel_app/images/standard_profile.jpg'
                    return render(request, "padre.html", {"url":default})
            else:
                return HttpResponse("Usuario incorrecto")
        else:
            return render(request, "login.html", {"form":form})

    form = AuthenticationForm()

    return render(request, "login.html", {"form":form})

def register(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "inicio.html", {"mensaje":"Usuario creado"})
        
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form":form})
            
@login_required
def editar_perfil(request):

    usuario = request.user

    if request.method == "POST":
        mi_formulario = UserEditForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            usuario.username = informacion['username']
            password = informacion['password_uno']
            usuario.set_password(password)
            usuario.save()

            return render(request, "inicio.html")


    else:
        mi_formulario = UserEditForm(initial={'username':usuario.username})

    return render(request, "editar_perfil.html", {'mi_formulario':mi_formulario, "usuario":usuario})



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