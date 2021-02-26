from django.db import models
from apps.medicamento.models import Medicamento
# Create your models here.

class Inventario(models.Model):
    cod_med = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return self.cod_med