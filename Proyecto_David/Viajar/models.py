from django.db import models

# Create your models here.

class Viaje(models.Model):
	Destino = models.CharField(max_length=30)
	Instrucciones = models.TextField()
	Salida = models.DateTimeField()
	Regreso = models.DateTimeField()
	NumNoches = models.CharField(max_length=2)

	def __str__(self):
		return '%s' % (self.Destino)
	
