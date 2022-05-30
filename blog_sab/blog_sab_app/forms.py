import datetime
from django import forms
from django.forms import ModelForm
from blog_sab_app.models import Estudio

class EstudioForm(forms.Form):
    universidad = forms.CharField(max_length=40, label='Universidad')
    anio_inicio = forms.IntegerField(label='Inicio')
    titulo = forms.CharField(max_length=40, label='Titulo')
    finalizado = forms.CharField(max_length=2, label='Finalizado')

class ViajesForm(forms.Form):
    destino = forms.CharField(max_length=40, label='Destino')
    nro_vuelo = forms.IntegerField(label='Vuelo')
    fecha = forms.DateField(label='Fecha', widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))
    notas = forms.CharField(max_length=200, label='Notas')

class EmpleosForm(forms.Form):
    empresa = forms.CharField(max_length=30, label='Empresa')
    periodo = forms.IntegerField(label='Período')
    puesto = forms.CharField(max_length=40, label='Puesto')
