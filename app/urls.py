from django.urls import path
from .views import home, terminos, registro

urlpatterns = [
    path('', home, name="home"),
    path('terminos/', terminos, name="terminos"),
    path('registro/', registro, name="registro"),

]
