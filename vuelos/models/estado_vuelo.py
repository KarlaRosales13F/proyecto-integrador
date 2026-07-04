from django.db import models
from .vuelo import Vuelo

class EstadoVuelo(models.Model):
    vuelo       = models.ForeignKey(Vuelo, on_delete=models.CASCADE, related_name='historial_estados')
    estado      = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True)
    fecha       = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = 'Estado de Vuelo'
        verbose_name_plural = 'Estados de Vuelo'
        ordering            = ['-fecha']

    def __str__(self):
        return f'{self.vuelo} — {self.estado} ({self.fecha:%d/%m/%Y %H:%M})'
