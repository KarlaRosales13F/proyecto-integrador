from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from vuelos.models import MantenimientoAeronave
from vuelos.serializers import MantenimientoAeronaveSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura

class MantenimientoAeronaveViewSet(viewsets.ModelViewSet):
    queryset           = MantenimientoAeronave.objects.select_related('aeronave').all()
    serializer_class   = MantenimientoAeronaveSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields   = ['aeronave', 'tipo', 'estado']
    search_fields      = ['descripcion', 'tecnico_responsable']
    ordering_fields    = ['fecha_inicio', 'costo', 'estado']
