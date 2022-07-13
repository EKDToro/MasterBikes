from django.urls import path
from .views import *

urlpatterns = [
    path('productos/',product_list),
    path('productos/<str:product_id>',product_detail),
    path('marcas/',marca_list)
]