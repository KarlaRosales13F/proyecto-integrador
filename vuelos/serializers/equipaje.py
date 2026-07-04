from rest_framework import serializers
from vuelos.models import Equipaje

class EquipajeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Equipaje
        fields = ['id', 'reserva', 'tipo', 'peso_kg', 'descripcion']
