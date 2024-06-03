from django.shortcuts import render

def mensaje(request):
    return render(request, 'mensaje.html')

def funcion_nombre(request):
    nombre = 'Halia'
    return render(request, 'nombre.html',{'nombre':nombre})
    