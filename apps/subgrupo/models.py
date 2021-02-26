from django.db import models

# Create your models here.

class Subgrupo(models.Model):
    nombre_subgrupo = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre_subgrupo