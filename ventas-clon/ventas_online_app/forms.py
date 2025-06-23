from django.forms import ModelForm
from .models import Products


class ProductsForm(ModelForm):  #Por convencion de nombres el nombre del formulario debe ser el mismo que el del modelo
    class Meta:
        model = Products
        fields = ['name', 'description', 'stock', 'price', 'image']
    
    

