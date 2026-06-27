from django.db import models
from .reserva import Reserva

class FeedbackPasajero(models.Model):
    reserva              = models.OneToOneField(Reserva, on_delete=models.CASCADE, related_name='feedback')
    calificacion         = models.PositiveSmallIntegerField(help_text='Calificación del 1 al 5')
    comentario           = models.TextField(blank=True)
    puntualidad          = models.PositiveSmallIntegerField(default=3, help_text='Del 1 al 5')
    atencion_tripulacion = models.PositiveSmallIntegerField(default=3, help_text='Del 1 al 5')
    comodidad            = models.PositiveSmallIntegerField(default=3, help_text='Del 1 al 5')
    fecha_feedback       = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = 'Feedback de Pasajero'
        verbose_name_plural = 'Feedbacks de Pasajeros'
        ordering            = ['-fecha_feedback']

    def __str__(self):
        return f'Feedback Reserva #{self.reserva_id} — {self.calificacion}/5'
