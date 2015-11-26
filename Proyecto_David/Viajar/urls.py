from django.conf.urls import url
from Viajar import views

urlpatterns = [
   url(r'^$', views.indice, name='indice'),
	url(r'^ediciones/(?P<viaje_id>\d+)/$',views.ediciones, name='ediciones'), #
	url(r'^registro$', views.registro, name='registro'),
	url(r'^login$', views.loginpage, name='login'),
	url(r'^logout$', views.logoutpage, name='logout'),
] #Las url son las diferentes paginas que tengo.
