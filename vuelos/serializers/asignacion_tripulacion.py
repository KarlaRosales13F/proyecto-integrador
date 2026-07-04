from rest_framework import serializers
from vuelos.models import AsignacionTripulacion

class AsignacionTripulacionSerializer(serializers.ModelSerializer):
    tripulacion_nombre = serializers.CharField(source='tripulacion.__str__', read_only=True)
    vuelo_info = serializers.CharField(source='vuelo.__str__', read_only=True)

    class Meta:
        model  = AsignacionTripulacion
        fields = ['id', 'vuelo', 'vuelo_info', 'tripulacion', 'tripulacion_nombre', 'fecha_asignacion']
        read_only_fields = ['fecha_asignacion']
