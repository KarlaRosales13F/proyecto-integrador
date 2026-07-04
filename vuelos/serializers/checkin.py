from rest_framework import serializers
from vuelos.models import CheckIn


class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ['id', 'reserva', 'hora_checkin', 'puerta', 'tarjeta_embarque', 'estado']
        read_only_fields = ['hora_checkin']
