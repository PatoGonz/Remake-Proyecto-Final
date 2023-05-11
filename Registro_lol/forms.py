from django import forms

class CampeonForm(forms.Form):
    nombre = forms.CharField(max_length=15)
    descripcion = forms.CharField(max_length=25)
    dificultad = forms.CharField(max_length=7)
    fecha_creacion = forms.DateField()    

class BuscarCampeonesForm(forms.Form):
    criterio_nombre = forms.CharField(max_length=15)