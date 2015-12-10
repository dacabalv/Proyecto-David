from django.conf.urls import url
from Viajar import views

urlpatterns = [
   url(r'^$', views.indice, name='indice'),
	url(r'^ediciones/(?P<viaje_id>\d+)/$',views.ediciones, name='ediciones'), #a esta url le doy el nombre de ediciones.
	url(r'^seleccion/(?P<edicion_id>\d+)/$',views.selecciones, name='selecciones'), # a esta la llamo selecciones , para la edicion que eligen.
	url(r'^reserva_usuario$',views.reservas_usuario, name='reservas_usuario'),
	url(r'^registro$', views.registro, name='registro'),
	url(r'^login$', views.loginpage, name='login'),
	url(r'^logout$', views.logoutpage, name='logout'),
] #Las url son las diferentes paginas que tengo.
