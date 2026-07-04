from django.db import models
from .terminal import Terminal

class Puerta(models.Model):
    terminal = models.ForeignKey(Terminal, on_delete=models.PROTECT, related_name='puertas')
    codigo   = models.CharField(max_length=10)
    activa   = models.BooleanField(default=True)

    class Meta:
        verbose_name        = 'Puerta'
        verbose_name_plural = 'Puertas'
        ordering            = ['terminal', 'codigo']
        unique_together     = [['terminal', 'codigo']]

    def __str__(self):
        return f'Puerta {self.codigo} — {self.terminal}'
