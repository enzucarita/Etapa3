from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def terminos(request):
    return render(request, 'app/terminos.html')



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