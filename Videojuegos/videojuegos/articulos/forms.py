from django import forms
from articulos.models import Articulos, Categoria

class FormArticulo(forms.ModelForm):

    class Meta:
        model = Articulos
        #fields = ['nombre', 'genero', 'stock']
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'stock': forms.NumberInput(attrs={'class':'form-control'}),
            'genero': forms.Select(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
        }   
        #exclude = 'stock'

class FormCategoria(forms.ModelForm):

    class Meta:
        model = Categoria
        #fields = ['nombre', 'genero', 'stock']
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
    
        }   
        #exclude = 'stock'