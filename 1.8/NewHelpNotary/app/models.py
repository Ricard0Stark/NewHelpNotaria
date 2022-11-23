from django.db import models

# Create your models here.



opciones_consulta = [
    [0, "consulta"],
    [1, "reclamo "],
    [2, "sugerencia"],
    [3, "otro"],
    
]
class contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField(null=True)

    def __str__(self):
        
        return self.nombre