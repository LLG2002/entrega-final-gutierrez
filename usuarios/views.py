from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import FormularioCreacion, EditarUsuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import InfoExtra
from django.contrib.auth.mixins import LoginRequiredMixin


def registrarse(request):
    if request.method == "POST":
        formulario = FormularioCreacion(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios:login')
        else:
            return render(request, 'inicio/registrar.html', {'formulario': formulario})
    
    formulario = FormularioCreacion()
    return render(request, 'inicio/registrar.html', {'formulario': formulario})


def login(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            usuario = authenticate(username=nombre_usuario, password=contrasenia)
            django_login(request, usuario)
            InfoExtra.objects.get_or_create(user= request.user)
            return redirect('inicio_principal:inicio')
        else:
            return render(request, 'inicio/login.html', {'formulario': formulario})
            
        
    formulario = AuthenticationForm()
    return render(request, 'inicio/login.html', {'formulario': formulario})

@login_required 
def editar_usuario(request):
    
    if request.method == "POST":
        formulario = EditarUsuario(request.POST, request.FILES, instance=request.user)
        
        if formulario.is_valid():
            if formulario.cleaned_data.get('avatar'):
                request.user.infoextra.avatar = formulario.cleaned_data.get('avatar')
            request.user.infoextra.save()
            formulario.save()
            return redirect('inicio_principal:inicio')
        
        else:
            return render(request, 'inicio/editar_usuario.html', {'formulario': formulario})
    
    formulario = EditarUsuario(initial={'avatar' : request.user.infoextra.avatar}, instance=request.user)
    return render(request, 'inicio/editar_usuario.html', {'formulario': formulario})

class CambiarContrasenia(LoginRequiredMixin,PasswordChangeView):
    template_name= 'inicio/cambiar_contrasenia.html'
    success_url= reverse_lazy('usuarios:login')
    
@login_required 
def mostrar_usuario(request):
    ...
    return render(request, 'inicio/perfil.html', {'user': request.user})
    

