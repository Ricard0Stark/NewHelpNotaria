from django.shortcuts import render
from .forms import ContactoForm

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

    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid(): 
            formulario.save()
            data["mensaje"]= "mensaje exitoso"
        else:
            data["form"] = formulario
                
    return render (request, 'app/Contacto.html',data)






