from django.db import models

# Create your models here.

class Estudiante(models.Model):

    nombre=models.CharField(max_length=50,verbose_name="Nombre")

    parcial1=models.FloatField()
    parcial2=models.FloatField()
    parcial3=models.FloatField()
    promedio=models.FloatField()
