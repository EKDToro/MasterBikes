from django.shortcuts import render, redirect
from django.http import HttpResponse
from crud.models import Producto

# Create your views here.

def root(request):
    return redirect('/home')

def home(request):
    return render(request,'core/home.html')

def productos(request):
    context = {'productos':Producto.objects.all()}
    return render(request,'core/productos.html',context)

def product_by_marca(request,marca):
    context = {'productos':Producto.objects.filter(marca=marca)}
    return render(request,'core/productos.html',context)

def contacto(request):
    return render(request,'core/contacto.html')

def nosotros(request):
    return render(request,'core/nosotros.html')
