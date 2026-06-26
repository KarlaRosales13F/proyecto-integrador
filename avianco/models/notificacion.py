from django.db import models
from django.contrib.auth.models import User

class Notificacion(models.Model):

    class Tipo(models.TextChoices):
        INFO     = 'info',     'Información'
        ALERTA   = 'alerta',   'Alerta'
        CANCELADO = 'cancelado', 'Cancelación'
        EMBARQUE = 'embarque', 'Embarque'

    usuario  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notificaciones')
    tipo     = models.CharField(max_length=20, choices=Tipo.choices, default=Tipo.INFO)
    titulo   = models.CharField(max_length=200)
    mensaje  = models.TextField()
    leida    = models.BooleanField(default=False)
    fecha    = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = 'Notificación'
        verbose_name_plural = 'Notificaciones'
        ordering            = ['-fecha']

    def __str__(self):
        return f'{self.titulo} — {self.usuario.username}'
