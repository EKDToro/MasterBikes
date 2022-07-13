from django.shortcuts import render,redirect,reverse
from .models import *
from .forms import *

# Create your views here.

def product_list(request):
    context = {'productos':Producto.objects.all()}
    return render(request,'crud/product-list.html',context)

def product_by_marca(request,marca):
    context = {'productos':Producto.objects.filter(marca=marca)}
    return render(request,'crud/product-list.html',context)

def product_new(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST,request.FILES)
        if form.is_valid():
            idProducto = form.cleaned_data.get("idProducto")
            descripcion = form.cleaned_data.get("descripcion")
            precio = form.cleaned_data.get("precio")
            stock = form.cleaned_data.get("stock")
            marca = form.cleaned_data.get("marca")
            imagen = form.cleaned_data.get("imagen")
            obj = Producto.objects.create(
                idProducto=idProducto,
                descripcion=descripcion,
                precio=precio,
                stock=stock,
                marca=marca,
                imagen=imagen
            )
            obj.save()
            return redirect(reverse('product-list') + "?OK")
        else:
            return redirect(reverse('product-list') + "?FAIL")
    else:
        form = ProductoForm
    return render(request,'crud/product-new.html',{'form':form})

def product_detail(request,product_id):
    try:
        producto = Producto.objects.get(idProducto=product_id)
        if producto:
            context = {'producto':producto}
            return render(request,'crud/product-detail.html',context)
    except:
        return redirect(reverse('product-list') + "?FAIL")

def product_edit(request,product_id):
    try:
        producto = Producto.objects.get(idProducto=product_id)
        form = ProductoForm(instance=producto)

        if request.method == 'POST':
            form = ProductoForm(request.POST,request.FILES,instance=producto)
            if form.is_valid():
                form.save()
                return redirect(reverse('product-list') + '?UPDATED')
            else:
                return redirect(reverse('product-edit') + product_id)

        context = {'form':form}
        return render(request,'crud/product-edit.html',context)
    except:
        return redirect(reverse('product-list') + "?NO_EXITS")

def product_delete(request,product_id):
    try:
        producto = Producto.objects.get(idProducto=product_id)
        producto.delete()
        return redirect(reverse('product-list') + "?OK")
    except:
        return redirect(reverse('product-list') + "?FAIL")