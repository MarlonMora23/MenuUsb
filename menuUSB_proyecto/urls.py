"""
URL configuration for menuUSB_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from  tiendas_app.views import listViewProduct, createProduct, readProduct, updateProduct, deleteProduct
from  tiendas_app.views import listViewStore, createStore, readStore, updateStore, deleteStore
from tiendas_app import views
from usuarios_app import views as login
from usuarios_app.views import *

#from  usuarios_app.views import listViewProduct, createProduct, readProduct, updateProduct, deleteProduct
#from usuarios_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', listViewProduct.as_view(template_name = "accounts/login.html"), name='leer'),
    path('', views.home_redirect, name='home_redirect'),
    path('login', login.usuarioIngreso, name='login'),
  
    path('home', views.home_view, name='index'),
    path('catalogo', views.catalogue_view, name='catalogo'),
    #Tiendas 
    path('stores/', listViewStore.as_view(template_name = "stores/index.html"), name='stores'),
    path('stores/detalle/<int:pk>', readStore.as_view(template_name = "stores/detalles.html"), name='detalles'),
    path('stores/crear', createStore.as_view(template_name = "stores/crear.html"), name='crear'),
    path('stores/editar/<int:pk>', updateStore.as_view(template_name = "stores/actualizar.html"), name='actualizar'), 
    path('stores/eliminar/<int:pk>', deleteStore.as_view(), name='eliminar'),
    #Productos 
    path('products/', listViewProduct.as_view(template_name = "products/index.html"), name='products'),
    path('products/detalle/<int:pk>', readProduct.as_view(template_name = "products/detalles.html"), name='detalles'),
    path('products/crear', createProduct.as_view(template_name = "products/crear.html"), name='crear'),
    path('products/editar/<int:pk>', updateProduct.as_view(template_name = "products/actualizar.html"), name='actualizar'), 
    path('products/eliminar/<int:pk>', deleteProduct.as_view(), name='eliminar'),

]