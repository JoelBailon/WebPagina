from django.shortcuts import render
from .models import Usuarios

def lista_usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'TransPorto/lista_usuarios.html', {'usuarios': usuarios})

def index(request):
    return render(request, 'TransPorto/index.html')