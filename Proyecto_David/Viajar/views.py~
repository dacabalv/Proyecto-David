from django.shortcuts import render,get_object_or_404
from Viajar.forms import ComentarioForm
from Viajar.models import Viaje,Edicion #aquí importo los del models.
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
#Aquí en el views hago las consultas sobre el models y se lo paso a los html.

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

@login_required
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

@login_required
def logoutpage(request):
	logout(request)
	return HttpResponseRedirect("/")

def ediciones(request,viaje_id): #viaje_id es la clave primaria que te crea django por defecto.
	if request.method == "POST":
		form = ComentarioForm(request.POST)
		if form.is_valid():
			comentario = form.save()
			comentario.save()
			return HttpResponseRedirect("/")
	else:
		form = ComentarioForm()
		ediciones = Edicion.objects.filter(viaje=viaje_id ) #De todas las ediciones, que me coja solamente las del viaje que selecciono.
	return render (request, 'Viajar/ediciones.html', {'ediciones': ediciones,'form':form,})	#con esto le digo que me lleve al html(me lo saca en la pagina)

@login_required
def selecciones(request,edicion_id):
	edicion = get_object_or_404(Edicion, pk = edicion_id)	
	edicion.usuarios.add(request.user)
	edicion.n_plazas = edicion.n_plazas-1  #este decrementa el numero de plazas cada vez que reserva un usuario una edicion.
	edicion.save()
	reservas = Edicion.objects.filter(usuarios__in=[request.user.id])
	return render (request, 'Viajar/reserva.html', {'reservas': reservas,})

@login_required
def reservas_usuario(request):
	reservas = Edicion.objects.filter(usuarios__in=[request.user.id])
	return render (request, 'Viajar/reserva.html', {'reservas': reservas,})

	
	

