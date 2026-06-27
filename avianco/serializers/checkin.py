from rest_framework import serializers
from vuelos.models import CheckIn

class CheckInSerializer(serializers.ModelSerializer):
    reserva_info  = serializers.CharField(source='reserva.__str__', read_only=True)
    metodo_display = serializers.CharField(source='get_metodo_display', read_only=True)

    class Meta:
        model  = CheckIn
        fields = [
            'id', 'reserva', 'reserva_info',
            'fecha_checkin',
            'metodo', 'metodo_display',
            'asiento_final', 'equipaje_listo', 'pase_abordar'
        ]
        read_only_fields = ['fecha_checkin']
