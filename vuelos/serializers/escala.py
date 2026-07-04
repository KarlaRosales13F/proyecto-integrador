from rest_framework import serializers
from vuelos.models import Escala

class EscalaSerializer(serializers.ModelSerializer):
    aeropuerto_nombre = serializers.CharField(source='aeropuerto.nombre', read_only=True)

    class Meta:
        model  = Escala
        fields = ['id', 'vuelo', 'aeropuerto', 'aeropuerto_nombre', 'orden', 'llegada', 'salida']
