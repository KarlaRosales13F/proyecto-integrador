from rest_framework import serializers
from vuelos.models import Tripulacion

class TripulacionSerializer(serializers.ModelSerializer):
    nombre_completo = serializers.SerializerMethodField()

    class Meta:
        model  = Tripulacion
        fields = ['id', 'nombre', 'apellido', 'nombre_completo', 'rol', 'licencia', 'activo']

    def get_nombre_completo(self, obj):
        return f'{obj.nombre} {obj.apellido}'
