from django import forms
from Viajar.models import Comentario

class ComentarioForm(forms.ModelForm):

	class Meta:
		model = Comentario
		fields = ('opinion',)



