from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# En cada modelo django crea un ...._id para cada viaje,usuario,edicion...

class Viaje(models.Model):
	continente = models.CharField(max_length=30,default='Africa')
	pais = models.CharField(max_length=30,default='Mali')
	lugar = models.CharField(max_length=30,default='capital')
	tipo = models.CharField(max_length=30,default='avion')
	precio = models.CharField(max_length=10,default='nulo')
	plazas_disponibles = models.CharField(max_length=20,default='0')
	foto = models.ImageField(upload_to='Viajar/static/media',null=True) #null=true es para que no de error si el campo está vacio.
	descripcion = models.TextField(null=True)
	
	

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
	n_plazas = models.IntegerField()
	viaje = models.ForeignKey(Viaje)
	usuarios = models.ManyToManyField(User,null=True) #quiero sacar las ediciones que tiene el usuario actual y pasarselas al html reservas.
#Lista de usuarios que tienen hecha una edicion

	def __str__(self):
		return '%s' % (self.viaje)


	class Meta:
		verbose_name = 'edición'# El nombre del modelo
		verbose_name_plural = 'ediciones'# El nombre en plural




class Comentario(models.Model):
	opinion = models.TextField()
	usuario = models.ForeignKey(User,null=True)
	viaje =models.ForeignKey(Viaje,default=1)
	
