from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    edad = models.IntegerField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
