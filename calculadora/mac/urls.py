from django.urls import path
<<<<<<< HEAD
from .views import  funcion_hola, funcion_calculadora
=======
from .views import funcion_hola, funcion_calculadora

>>>>>>> ded7fc8b56ed4d9ca623f4d6bd1656e084ad7498

urlpatterns = [
    path('hola/', funcion_hola),
    path('calculadora/', funcion_calculadora),
]
