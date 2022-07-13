from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Marca(models.Model):
    marca = models.CharField(verbose_name='Marca',max_length=50)
    creado = models.DateTimeField(verbose_name='Fecha creación',auto_now_add=True)
    actualizado = models.DateTimeField(verbose_name='Fecha actualización',auto_now=True)

    class Meta:
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'

    def __str__(self):
        return self.marca

class Producto(models.Model):
    idProducto = models.CharField(primary_key=True,verbose_name='ID',max_length=20)
    descripcion = models.CharField(verbose_name='Descripción',max_length=250)
    precio = models.IntegerField(verbose_name='Precio Unitario')
    stock = models.IntegerField(verbose_name='Stock')
    imagen = models.ImageField(verbose_name='Imagen',upload_to='productos',null=True,blank=True)
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE)
    creado = models.DateTimeField(verbose_name='Fecha creación',auto_now_add=True)
    actualizado = models.DateTimeField(verbose_name='Fecha actualización',auto_now=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return self.descripcion