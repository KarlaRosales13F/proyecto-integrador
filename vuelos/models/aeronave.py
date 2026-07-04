from django.db import models


class Aeronave(models.Model):
    matricula  = models.CharField(max_length=20, unique=True)
    modelo     = models.CharField(max_length=100)
    capacidad  = models.PositiveIntegerField()

    class Meta:
        verbose_name        = 'Aeronave'
        verbose_name_plural = 'Aeronaves'
        ordering            = ['modelo']

    def __str__(self):
        return f'{self.matricula} ({self.modelo})'