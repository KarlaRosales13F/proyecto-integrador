from django.db import models

class Tripulacion(models.Model):

    class Rol(models.TextChoices):
        PILOTO      = 'piloto',      'Piloto'
        COPILOTO    = 'copiloto',    'Copiloto'
        AZAFATA     = 'azafata',     'Azafata'
        TECNICO     = 'tecnico',     'Técnico'

    nombre    = models.CharField(max_length=150)
    apellido  = models.CharField(max_length=150)
    rol       = models.CharField(max_length=20, choices=Rol.choices)
    licencia  = models.CharField(max_length=50, unique=True)
    activo    = models.BooleanField(default=True)

    class Meta:
        verbose_name        = 'Tripulación'
        verbose_name_plural = 'Tripulación'
        ordering            = ['apellido', 'nombre']

    def __str__(self):
        return f'{self.nombre} {self.apellido} ({self.get_rol_display()})'
