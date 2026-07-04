from rest_framework import serializers
from vuelos.models import Puerta

class PuertaSerializer(serializers.ModelSerializer):
    terminal_nombre = serializers.CharField(source='terminal.nombre', read_only=True)

    class Meta:
        model  = Puerta
        fields = ['id', 'terminal', 'terminal_nombre', 'codigo', 'activa']
