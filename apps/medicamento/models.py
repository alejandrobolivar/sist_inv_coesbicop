from django.db import models
from apps.laboratorio.models import Laboratorio
from apps.grupo.models import Grupo
from apps.subgrupo.models import Subgrupo
# Create your models here.

class Medicamento(models.Model):
    cod_med = models.CharField(max_length=10, default='')
    principio_activo_med = models.CharField(max_length=200)
    nombre_comercial_med = models.CharField(max_length=200)
    nombre_lab_med =models.ForeignKey(Laboratorio, on_delete=models.CASCADE, default='')
    presentación_med = models.CharField(max_length=200)
    dosis_med = models.CharField(max_length=200)
    via_admon_med = models.CharField(max_length=200)
    grupo_med = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    subgrupo_med = models.ForeignKey(Subgrupo, on_delete=models.CASCADE)
    fecha_vencimiento_med=models.DateTimeField('Fecha de vencimiento')
    
    def __str__(self):
        return self.cod_med
