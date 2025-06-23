from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("/lista_productos", views.list_products, name="lista_productos"),
    path("product/<int:product_id>/", views.product_detail, name="product_detail"),
    path("add_product/",views.add_product_form, name="add_product_form"),
    path('register/', views.register, name='register'),
     path('ubicacion/', views.ubicacion, name='ubicacion')
    
]