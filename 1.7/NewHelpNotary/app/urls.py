from django.urls import path
from .views import home ,Equipo , Tramites , Servicios , PreguntasFrecuentes , ReservarHora , ReservarHoraClientes , Contacto

urlpatterns = [
    path('', home, name ="home" ),
    path('Equipo',Equipo, name ="Equipo" ),
    path('Tramites',Tramites, name ="Tramites" ),
    path('Servicios',Servicios, name ="Servicios" ),
    path('PreguntasFrecuentes',PreguntasFrecuentes, name ="PreguntasFrecuentes" ),
    path('ReservarHora',ReservarHora, name ="ReservarHora" ),
    path('ReservarHoraClientes',ReservarHoraClientes, name ="ReservarHoraClientes" ),
    path('Contacto',Contacto, name ="Contacto" ),





]
