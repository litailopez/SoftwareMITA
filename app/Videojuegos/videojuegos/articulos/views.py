from django.shortcuts import render, redirect
from articulos.models import Articulos
from articulos.forms import FormArticulo

# URLConf -> MVT
def lista_articulos(request):
    articulos = Articulos.objects.all()
    #select * from articulos_articulos;

    return render(request, 'articulos.html', {'articulos':articulos})

def eliminar_articulos(request, id):
    Articulos.objects.get(id=id).delete()
    return redirect('articulos_lista')

def nuevo_articulo(request):
    if request.method == 'POST':
        form = FormArticulo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articulos_lista')
    else:
        form = FormArticulo()
    return render(request, 'nuevo_articulo.html', {'form':form} )

def editar_articulos(request, id):
    articulo = Articulos.objects.get(id=id)
    if request.method == 'POST':
        form = FormArticulo(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('articulos_lista')
    else:
        form = FormArticulo(instance=articulo)
    return render(request, 'editar_articulo.html', {'form':form} )