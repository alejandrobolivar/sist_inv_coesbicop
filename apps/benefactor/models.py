from django.db import models

# Create your models here.

class Benefactor(models.Model):
    cod_benefactor = models.CharField(max_length=10, default='')
    nombre_benefactor = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre_benefactor
    