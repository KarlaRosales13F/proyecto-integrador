from rest_framework import serializers
from vuelos.models import DocumentoPasajero

class DocumentoPasajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model  = DocumentoPasajero
        fields = [
            'id', 'pasajero', 'tipo', 'numero',
            'pais_emisor', 'fecha_emision', 'fecha_vencimiento', 'activo'
        ]
