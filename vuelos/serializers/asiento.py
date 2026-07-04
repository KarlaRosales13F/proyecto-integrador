from rest_framework import serializers
from vuelos.models import Asiento


class AsientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asiento
        fields = ['id', 'vuelo', 'codigo', 'clase', 'fila', 'columna', 'disponible']
