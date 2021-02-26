from django.db import models

# Create your models here.

class Ingreso(models.Model):
    cod_benefactor = models.CharField(max_length=10, default='')
    fecha_recibido=models.DateTimeField('Fecha de recibido')
    cod_med = models.CharField(max_length=10, default='')
    cant_ingreso = models.IntegerField(default=0)
    
    def __str__(self):
        return self.cod_benefactor
