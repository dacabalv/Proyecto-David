from django.conf.urls import url
from Viajar import views

urlpatterns = [
   url(r'^$', views.indice, name='indice'),
]
