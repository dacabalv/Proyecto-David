from django.shortcuts import render
from Viajar.models import Viaje
# Create your views here.

def indice(request):
   Viajes = Viaje.objects.all()
   return render(request, 'Viajar/index.html', {'Viajes': Viajes })
