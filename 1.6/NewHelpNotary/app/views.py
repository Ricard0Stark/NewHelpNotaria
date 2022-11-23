from django.shortcuts import render

# Create your views here.

def home (request):
    return render (request, 'app/home.html')

def Equipo (request):
    return render (request, 'app/equipo.html')

def Tramites (request):
    return render (request, 'app/Tramites.html')

def Servicios (request):
    return render (request, 'app/Servicios.html')

def PreguntasFrecuentes (request):
    return render (request, 'app/PreguntasFrecuentes.html')

def ReservarHora (request):
    return render (request, 'app/ReservarHora.html')


def ReservarHoraClientes (request):
    return render (request, 'app/ReservarHoraClientes.html')

def Contacto (request):
    return render (request, 'app/Contacto.html')






