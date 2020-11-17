from django.urls import path
from .views import home, terminos, registro, galeria, agregar_producto, listar_productos
urlpatterns = [
    path('', home, name="home"),
    path('terminos/', terminos, name="terminos"),
    path('registro/', registro, name="registro"),
    path('galeria/', galeria, name="galeria"),  
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
]
