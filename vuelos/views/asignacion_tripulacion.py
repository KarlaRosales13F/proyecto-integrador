from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from vuelos.models import AsignacionTripulacion
from vuelos.serializers import AsignacionTripulacionSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura

class AsignacionTripulacionViewSet(viewsets.ModelViewSet):
    queryset           = AsignacionTripulacion.objects.select_related('vuelo', 'tripulacion').all()
    serializer_class   = AsignacionTripulacionSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, OrderingFilter]
    filterset_fields   = ['vuelo', 'tripulacion']
    ordering_fields    = ['fecha_asignacion']
