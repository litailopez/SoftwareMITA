from django.shortcuts import render

<<<<<<< HEAD
# Create your views here.
def funcion_hola(request):
    return render(request, "hola.html")

def funcion_calculadora(request):
    return render(request, "calculadora.html")
=======
def funcion_hola(request):
    return render(request, 'hola.html')

def funcion_calculadora(request):
    print (request.POST)
    resultado = '';
    if request.method == 'POST':
        num1 = int(request.POST.get('num1',0))
        num2 = int(request.POST.get('num2',0))
        operacion = request.POST.get('operacion',0)
        if operacion == '+':
            resultado = num1 + num2
        if operacion == '-':
            resultado = num1 - num2
        if operacion == 'X':
            resultado = num1 * num2
        if operacion == '/':
            resultado = num1 / num2 
    
    return render(request,'calculadora.html', {'resultado':resultado})
>>>>>>> ded7fc8b56ed4d9ca623f4d6bd1656e084ad7498
