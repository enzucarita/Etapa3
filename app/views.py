from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Producto
from .forms import ProductoForm 

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def terminos(request):
    return render(request, 'app/terminos.html')

def galeria(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/galeria.html',data)

def agregar_producto(request):

    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
                data["form"] = formulario

    return render(request, 'producto/agregar.html', data)

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method =='POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user )
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario  

    return render(request, 'registration/registro.html', data)

def listar_productos(request):
    productos = Producto.objects.all()

    data = {
        'productos': productos
    }
    return render(request, 'producto/listar.html', data)