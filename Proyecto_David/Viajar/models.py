from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Viaje(models.Model):
	continente = models.CharField(max_length=30,default='Africa')
	pais = models.CharField(max_length=30,default='Mali')
	lugar = models.CharField(max_length=30,default='capital')
	tipo = models.CharField(max_length=30,default='avion')
	precio = models.CharField(max_length=10,default='nulo')
	plazas_disponibles = models.CharField(max_length=20,default='0')
	
	

	def __str__(self):
		return '%s' % (self.lugar)

class Usuario(models.Model):
	nombre = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=30)
	dirección = models.CharField(max_length=70)
	email = models.CharField(max_length=25)
	telefono = models.CharField(max_length=9)
	pais = models.CharField(max_length=15)
	provincia = models.CharField(max_length=15)
	ciudad = models.CharField(max_length=15)
	user = models.OneToOneField(User)

	def __str__(self):
		return '%s' % (self.Nombre)


class Edicion(models.Model):
	fecha_salida = models.CharField(max_length=30)
	fecha_regreso = models.CharField(max_length=30)
	n_plazas = models.CharField(max_length=30)
	viaje = models.ForeignKey(Viaje)

	class Meta:
		verbose_name = 'edición'# El nombre del modelo
		verbose_name_plural = 'ediciones'# El nombre en plural

	def __str__(self): 
		return self.Edicion

	def __str__(self):
		return '%s' % (self.Edicion)


class Comentario(models.Model):
	opinion = models.TextField()
	usuario = models.ForeignKey(Usuario)
	
