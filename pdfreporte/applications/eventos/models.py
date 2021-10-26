from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# Create your models here.

class Cliente (models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Factura (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Fecha = models.DateField()

    def __str__(self):
        return self.cliente

class Categoria (models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Ticket (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Fecha = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    

class Eventos(models.Model):
    nombre = models.CharField(max_length=30)
    fecha =models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    lugar = models.CharField(max_length=30)

class Ventas (models.Model):
    precio_iva= models.IntegerField()
    precio_sin_iva= models.IntegerField()
    Cantidad_ticket = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    fecha = models.DateField()
    estado = models.BooleanField()
