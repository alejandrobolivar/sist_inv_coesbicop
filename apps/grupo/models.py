from django.db import models

# Create your models here.

class Grupo(models.Model):
    nombre_grupo = models.CharField(max_length=200)
    leyenda_grupo = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre_grupo
    