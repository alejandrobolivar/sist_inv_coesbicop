from django.db import models
# from apps.inventario.models import Inventario
# Create your models here.

class Entrega(models.Model):
    cod_beneficiado = models.CharField(max_length=10, default='')
    fecha_entrega=models.DateTimeField('Fecha de entrega')
    cod_med = models.CharField(max_length=10, default='')
    cant_entrega = models.IntegerField(default=0)

    def __str__(self):
        return self.cod_beneficiado