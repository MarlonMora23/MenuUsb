from django.shortcuts import redirect, render
from .models import Product
from .models import Store
from usuarios_app.models import Usuario
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

def home_redirect(request):
    return redirect('index')

def login_view(request):
    # Renderiza la plantilla de inicio de sesión
    return render(request, 'accounts/login.html')

def stores_view(request):
    return render(request, 'stores/index,html')

def products_view(request):
    return render(request,'products/index.html')

def home_view(request):
    return render(request, 'home/index.html')

def catalogue_view(request):
    # Obtener todos los productos de la base de datos
    products = Product.objects.all()

    # Pasar la lista de productos al contexto de renderizado
    context = {
        'products': products
    }

    # Renderizar la plantilla catalogue.html con el contexto
    return render(request, 'home/catalogo.html', context)



#Vistas para Productos
class listViewProduct(ListView):
    model = Product 
    # def get_queryset(self):
    #     return Product.objects.filter(store=self.request.GET['store'])

class createProduct(SuccessMessageMixin, CreateView): 
    model = Product 
    form = Product 
    fields = "__all__" 
    success_message = 'Producto Creado Correctamente!'

    # Redireccionamos a la página principal luego de crear un producto
    def get_success_url(self):        
        return reverse('products') # Redireccionamos a la vista principal 'products'

class readProduct(DetailView): 
    model = Product 

class updateProduct(SuccessMessageMixin, UpdateView): 
    model = Product 
    form = Product 
    fields = "__all__" 
    success_message = 'Producto Actualizado Correctamente !'

    # Redireccionamos a la página principal luego de actualizar un producto
    def get_success_url(self):               
        return reverse('products') # Redireccionamos a la vista principal 'products'

class deleteProduct(SuccessMessageMixin, DeleteView): 
    model = Product 
    form = Product
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un producto
    def get_success_url(self): 
        success_message = 'Producto Eliminada Correctamente !' 
        messages.success (self.request, (success_message))       
        return reverse('products') # Redireccionamos a la vista principal 'products'


# Vistas para Tiendas
class listViewStore(ListView):
    model = Store
    #def get_queryset(self):
    #    return Store.objects.filter(admin=self.request.GET['admin'])

class createStore(SuccessMessageMixin, CreateView): 
    print(CreateView)
    model = Store 
    form = Store 
    fields = "__all__" 
    print(form)
    success_message = 'Store Creado Correctamente!'

    # Redireccionamos a la página principal luego de crear un Storeo
    def get_success_url(self):        
        return reverse('stores') # Redireccionamos a la vista principal 'store'

class readStore(DetailView): 
    model = Store 

class updateStore(SuccessMessageMixin, UpdateView): 
    model = Store 
    form = Store 
    fields = "__all__" 
    success_message = 'Store Actualizado Correctamente !'

    # Redireccionamos a la página principal luego de actualizar un Storeo
    def get_success_url(self):               
        return reverse('stores') # Redireccionamos a la vista principal 'leer'

class deleteStore(SuccessMessageMixin, DeleteView): 
    model = Store 
    form = Store
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un Storeo
    def get_success_url(self): 
        success_message = 'Store Eliminada Correctamente !' 
        messages.success (self.request, (success_message))       
        return reverse('stores') # Redireccionamos a la vista principal 'leer'
 