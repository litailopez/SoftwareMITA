from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect 

from articulos.forms import FormCategoria
from articulos.models import Articulos, Categoria
from articulos.forms import FormArticulo


class ListaCategorias(ListView):
    model = Categoria


class BienvenidaView(TemplateView):
    template_name = 'bienvenida.html'

class NuevaCategoriaView(CreateView):
    model = Categoria
    form_class = FormCategoria
    #fields = '__all__'
    success_url = reverse_lazy('categorias_lista')
    extra_context = {'accion' : 'Nueva'}

class EditarCategoriaView(UpdateView):
    model = Categoria
    form_class = FormCategoria
    #fields = '__all__'
    success_url = reverse_lazy('categorias_lista')
    extra_context = {'accion' : 'Modificar'}

class EliminarCategoriaView(DeleteView):
    model = Categoria
    success_url = reverse_lazy('categorias_lista')

    def form_valid(self, form):
        self.object = self.get_object()
        if Articulos.objects.filter(categoria=self.object):
            messages.error(self.request, 'No se puede eliminar la categoria')
        else:
            self.object.delete()
            messages.success(self.request, 'Eliminado correctamente')

        success_url = self.get_success_url()    
        return HttpResponseRedirect(self.success_url)    
