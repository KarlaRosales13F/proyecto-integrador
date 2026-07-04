from rest_framework import serializers
from vuelos.models import Reserva


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Reserva
        fields = ['id', 'vuelo', 'pasajero', 'asiento', 'estado', 'fecha_reserva']
        read_only_fields = ['fecha_reserva']

    def validate(self, data):
        vuelo   = data.get('vuelo',   getattr(self.instance, 'vuelo',   None))
        asiento = data.get('asiento', getattr(self.instance, 'asiento', None))
        qs = Reserva.objects.filter(vuelo=vuelo, asiento=asiento)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError({'asiento': 'Este asiento ya está ocupado en este vuelo.'})
        return data