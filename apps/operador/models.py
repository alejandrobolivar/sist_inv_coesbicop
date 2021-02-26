from django.db import models

# Create your models here.

class Operador(models.Model):
    usuario_operador = models.CharField(max_length=200, default='')
    nombre_operador = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre_operador