from django.db import models

# Create your models here.

class Beneficiado(models.Model):
    cod_beneficiado = models.CharField(max_length=10)
    nombres_beneficiado = models.CharField(max_length=200)
    apellidos_beneficiado = models.CharField(max_length=200)
    email_beneficiado = models.CharField(max_length=200)
    usuario_operador = models.CharField(max_length=200)
    
    def __str__(self):
        return self.cod_beneficiado