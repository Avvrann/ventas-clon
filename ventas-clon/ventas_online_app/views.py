from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Products
from .forms import ProductsForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def index(request):
    return render(request, 'index.html')

def list_products(request):
    lista_productos = Products.objects.all()
    context = {'productos': lista_productos}
    return render(request, "lista_productos.html", context)

def product_detail(request, product_id):
    product = Products.objects.get(id=product_id)
    context = {'product': product}  
    return render(request, "product_detail.html", context) 

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente después del registro
            return redirect('index')  # Redirige a la página de inicio
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def ubicacion(request):
    # Coordenadas fijas de Nueva York
    latitude = 40.7128
    longitude = -74.0060

    context = {
        'latitude': latitude,
        'longitude': longitude,
    }
    return render(request, 'ubicacion.html', context)

@login_required
def add_product_form(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Guarda el producto en la base de datos
            return redirect('lista_productos')  # Redirige a la lista de productos después de guardar
    else:
        form = ProductsForm()
    return render(request, "add_product_form.html", {"form": form})