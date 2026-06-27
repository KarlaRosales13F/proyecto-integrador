from rest_framework import serializers
from vuelos.models import FeedbackPasajero

class FeedbackPasajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model  = FeedbackPasajero
        fields = [
            'id', 'reserva', 'calificacion', 'comentario',
            'puntualidad', 'atencion_tripulacion', 'comodidad',
            'fecha_feedback'
        ]
        read_only_fields = ['fecha_feedback']
