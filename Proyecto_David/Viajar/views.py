from django.shortcuts import render
from Viajar.models import Viaje,Edicion #aquí importo los del models.
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
# Create your views here.

def indice(request):
   Viajes = Viaje.objects.all()
   return render(request, 'Viajar/index.html', {'Viajes': Viajes })

def registro(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/")
	else:
		form = UserCreationForm()
	return render(request, "Viajar/registro.html", {
'form': form,})

def loginpage(request):
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
		return HttpResponseRedirect("/")
		
	else:
			form = AuthenticationForm()
	return render (request, "Viajar/login.html", {'form': form,})

def logoutpage(request):
	logout(request)
	return HttpResponseRedirect("/")

def ediciones(request,viaje_id): #viaje_id es la clave primaria que te crea django por defecto.
	ediciones = Edicion.objects.filter(viaje=viaje_id) #De todas las ediciones, que me coja solamente las del viaje que selecciono.
	return render (request, 'Viajar/ediciones.html', {'ediciones': ediciones,})	#con esto le digo que me lleve al html(me lo saca en la pagina)





