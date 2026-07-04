from rest_framework import serializers
from vuelos.models import Pasajero


class PasajeroSerializer(serializers.ModelSerializer):
    nombre_completo = serializers.SerializerMethodField()

    class Meta:
        model  = Pasajero
        fields = [
            'id', 'usuario', 'nombre_completo',
            'numero_pasaporte', 'nacionalidad',
            'fecha_nacimiento', 'telefono',
        ]

    def get_nombre_completo(self, obj):
        return obj.usuario.get_full_name()