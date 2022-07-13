from django import forms
from django.forms import ModelForm
from .models import *

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = [
            'idProducto',
            'descripcion',
            'precio',
            'stock',
            'marca',
            'imagen'
        ]
        labels = {
            'idProducto':'Código Producto',
            'descripcion':'Descripción',
            'precio':'Precio Unitario',
            'stock':'Stock',
            'marca':'Marca',
            'imagen':'Imagen'
        }
        widgets = {
            'idProducto':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'precio':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'stock':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'marca':forms.Select(attrs={'class':'form-control'}),
            'imagen':forms.FileInput(attrs={'class':'form-control'})
        }

class MarcaForm(ModelForm):
    pass