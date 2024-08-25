from django.db import models
from usuarios_app.models import Usuario

# Create your models here.

class Store(models.Model):
    id_store = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='DEFAULT VALUE')
    location = models.CharField(max_length=100, default='DEFAULT VALUE')
    description = models.TextField(default='DEFAULT VALUE')
    img = models.FileField()
    admin = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, default='DEFAULT VALUE')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')
    img = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
