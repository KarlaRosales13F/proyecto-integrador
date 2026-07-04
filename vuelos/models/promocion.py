from django.db import models

class Promocion(models.Model):
    codigo      = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField()
    descuento   = models.DecimalField(max_digits=5, decimal_places=2)
    activa      = models.BooleanField(default=True)
    fecha_inicio = models.DateField()
    fecha_fin    = models.DateField()

    class Meta:
        verbose_name        = 'Promoción'
        verbose_name_plural = 'Promociones'
        ordering            = ['-fecha_inicio']

    def __str__(self):
        return f'{self.codigo} — {self.descuento}% descuento'
