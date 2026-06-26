from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from vuelos.models import SolicitudServicio
from vuelos.serializers import SolicitudServicioSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura

class SolicitudServicioViewSet(viewsets.ModelViewSet):
    queryset           = SolicitudServicio.objects.select_related('reserva').all()
    serializer_class   = SolicitudServicioSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields   = ['reserva', 'tipo_servicio', 'estado']
    search_fields      = ['descripcion']
    ordering_fields    = ['fecha_solicitud', 'estado']
