from django.db import models

# Create your models here.

class Actividad (models.Model):
    NombrePartida = models.CharField(max_length=5000)
    Unidad = models.CharField(max_length=25)
    DesPartida = models.CharField(max_length=5000)
    FormaMedicion = models.CharField(max_length=5000)
    MetodoPago = models.CharField(max_length=5000)

    def Actividad(self):
        cadena = "{0}, {1}, {2}, {3}, {4}"
        return cadena.format(self.NombrePartida, self.Unidad, self.DesPartida, self.FormaMedicion, self.MetodoPago)

    def __str__(self):
        return self.Actividad()