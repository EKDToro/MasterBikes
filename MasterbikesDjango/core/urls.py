from django.urls import path
from .views import *

urlpatterns = [
    path('', root),
    path('home',home,name='home'),
    path('productos/', productos, name='productos'),
    path('productos/marca/<marca>',product_by_marca,name='productos-marca'),
    path('contacto/', contacto, name='contacto'),
    path('nosotros/', nosotros, name='nosotros'),
]