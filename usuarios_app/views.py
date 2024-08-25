from django.shortcuts import render, redirect

# Create your views here.
from .models import Usuario
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from tiendas_app.models import Store
#from usuarios.models import *

def homeAdmin_redirect(request):
    return redirect('indexAdmin')

def loginAdmin_view(request):
    # Renderiza la plantilla de inicio de sesión
    return render(request, 'account/loginUsuarios.html')

def homeAdmin_view(request):
    return render(request, 'account/indexAdmin.html')

def usuarioIngreso(request, *args, **kwargs):
    categorias = Store.objects.all()
    ingresar = request.POST
    context={'usr':"", 'nombre':'noRegistrado'}
    if(request.method == 'POST'):
        aux = Usuario(
            id_usuario = "",
            nombre= "",
            clave=ingresar.get('password'),
            correo = ingresar.get('email'),
        )
        nombre = ingresar.get('email')
        print("pass")
        print(ingresar.get('password'))
        if (aux.autenticarUsuario()):
            messages.success(request, f'¡Bienvenido {nombre}!')
            usr = aux.buscarUsuario()
            print(usr)
            context={'usr':usr, 'nombre':nombre}
            # return redirect(to='stores/?admin='+usr.id_usuario)
            return redirect(to='stores/')
        else:
            print("false")
            messages.info(request, 'Cuenta de usuario o contraseña invalida')
    return render(request, 'account/loginUsuarios.html', context)

def usuarioCerrarSesion(request, *args, **kwargs):
    return redirect(to='usuarios:ingreso')

def usuarioInicio(request, nombre):
    categorias = Categoria.objects.all()
    context={'categorias':categorias, 'nombre': nombre}
    return render(request, 'account/loginUsuarios.html', context, {})