import django_filters
from vuelos.models import Aeropuerto, Aeronave, Vuelo, Pasajero, Reserva


class AeropuertoFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    ciudad = django_filters.CharFilter(lookup_expr='icontains')
    pais   = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model  = Aeropuerto
        fields = ['pais']


class AeronaveFilter(django_filters.FilterSet):
    modelo        = django_filters.CharFilter(lookup_expr='icontains')
    capacidad_min = django_filters.NumberFilter(field_name='capacidad', lookup_expr='gte')
    capacidad_max = django_filters.NumberFilter(field_name='capacidad', lookup_expr='lte')

    class Meta:
        model  = Aeronave
        fields = ['modelo']


class VueloFilter(django_filters.FilterSet):
    precio_min    = django_filters.NumberFilter(field_name='precio', lookup_expr='gte')
    precio_max    = django_filters.NumberFilter(field_name='precio', lookup_expr='lte')
    fecha_desde   = django_filters.DateTimeFilter(field_name='fecha_salida', lookup_expr='gte')
    fecha_hasta   = django_filters.DateTimeFilter(field_name='fecha_salida', lookup_expr='lte')
    origen_iata   = django_filters.CharFilter(field_name='origen__codigo_iata', lookup_expr='iexact')
    destino_iata  = django_filters.CharFilter(field_name='destino__codigo_iata', lookup_expr='iexact')

    class Meta:
        model  = Vuelo
        fields = ['estado', 'origen', 'destino', 'aeronave']


class PasajeroFilter(django_filters.FilterSet):
    nacionalidad = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model  = Pasajero
        fields = ['nacionalidad']


class ReservaFilter(django_filters.FilterSet):
    class Meta:
        model  = Reserva
        fields = ['estado', 'vuelo', 'pasajero']