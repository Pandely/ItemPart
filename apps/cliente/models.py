from django.db import models

# Create your models here.
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cargo = models.CharField(max_length=500)
    telefono = models.IntegerField()
    correo = models.EmailField(max_length=100)
    empresa = models.CharField(max_length=100)
    ruc = models.IntegerField()
    otro = models.TextField()

    def __str__(self):
        return self.nombres