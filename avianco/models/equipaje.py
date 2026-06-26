from django.db import models
from .reserva import Reserva

class Equipaje(models.Model):

    class Tipo(models.TextChoices):
        CABINA     = 'cabina',     'Equipaje de Cabina'
        BODEGA     = 'bodega',     'Equipaje de Bodega'
        ESPECIAL   = 'especial',   'Equipaje Especial'

    reserva     = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name='equipajes')
    tipo        = models.CharField(max_length=20, choices=Tipo.choices, default=Tipo.CABINA)
    peso_kg     = models.DecimalField(max_digits=5, decimal_places=2)
    descripcion = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name        = 'Equipaje'
        verbose_name_plural = 'Equipajes'
        ordering            = ['reserva', 'tipo']

    def __str__(self):
        return f'{self.get_tipo_display()} — {self.peso_kg}kg — Reserva #{self.reserva.pk}'
