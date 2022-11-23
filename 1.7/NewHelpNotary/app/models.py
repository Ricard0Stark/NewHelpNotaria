from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class perfil(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='batman.png')

	def __str__(self):
		return f'Perfil de {self.user.username}'


class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	timestamp = models.DateTimeField(default=timezone.now)
	content = models.TextField()

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f'{self.user.username}: {self.content}'



	def __str__(self):
		return f'{self.from_user} to {self.to_user}'

	class Meta:
		indexes = [
		models.Index(fields=['from_user', 'to_user',]),
		]





class usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    edad = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)



class secretaria(models.Model):
    id_secretaria = models.BigIntegerField()
    descripcion  = models.CharField(max_length=50)



class abogado(models.Model):
    id_secretaria = models.BigIntegerField()
    descripcion  = models.CharField(max_length=50)



class administrador(models.Model):
    id_secretaria = models.BigIntegerField()
    descripcion  = models.CharField(max_length=50)

class cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    edad = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    tarjeta = models.CharField(max_length=50)


class boleta(models.Model):
    numero_boleta = models.BigIntegerField()
    fecha_emision = models.CharField(max_length=100)
    tarjeta = models.CharField(max_length=50)
    numero_transaccion = models.BigIntegerField()




class documento(models.Model):
    codigo_documento = models.BigIntegerField()
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=50)
    precio = models.BigIntegerField()





class detalle_documento(models.Model):
    id_documento = models.BigIntegerField()
    estado_descripcion = models.CharField(max_length=100)
    firma = models.CharField(max_length=50)
    precio = models.BigIntegerField()







class registro_historico(models.Model):
    id_registro = models.BigIntegerField()
    nu_de_registros = models.BigIntegerField()
    ingresos_generados = models.BigIntegerField()
    num_formularios_rellenados = models.BigIntegerField()
    num_documentos_validados = models.BigIntegerField()
    num_tarjetas_registradas = models.BigIntegerField()
    visitas_pagina = models.BigIntegerField()
    


class reserva(models.Model):
    num_reserva = models.BigIntegerField()
    horario = models.CharField(max_length=100)
  
