from django import forms
from .models import contacto



class ContactoForm(forms.ModelForm):

    class Meta:
        model = contacto
        #fields =["nombre", "correo", "tipo_consulta", "mensaje"]
        fields = '__all__'
