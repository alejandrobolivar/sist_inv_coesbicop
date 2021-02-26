from django.db import models

# Create your models here.

class Laboratorio(models.Model):
    nombre_lab = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre_lab
