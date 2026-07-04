from rest_framework import serializers
from vuelos.models import Terminal

class TerminalSerializer(serializers.ModelSerializer):
    aeropuerto_nombre = serializers.CharField(source='aeropuerto.nombre', read_only=True)

    class Meta:
        model  = Terminal
        fields = ['id', 'aeropuerto', 'aeropuerto_nombre', 'nombre', 'descripcion']
