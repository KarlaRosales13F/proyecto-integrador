from rest_framework import serializers
from vuelos.models import SolicitudServicio

class SolicitudServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model  = SolicitudServicio
        fields = ['id', 'reserva', 'tipo_servicio', 'descripcion', 'estado', 'fecha_solicitud']
        read_only_fields = ['fecha_solicitud']
