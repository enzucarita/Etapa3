from django.urls import path
from td import views
from .views import home, terminos, registro, galeria, agregar_producto, listar_productos, modificar_producto, eliminar_producto, ubicacion
urlpatterns = [
    path('', home, name="home"),
    path('terminos/', terminos, name="terminos"),
    path('registro/', registro, name="registro"),
    path('galeria/', galeria, name="galeria"),  
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('ubicacion/', ubicacion, name="ubicacion"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', views.hello),
]

