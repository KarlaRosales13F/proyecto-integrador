from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from vuelos.models import DocumentoPasajero
from vuelos.serializers import DocumentoPasajeroSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura

class DocumentoPasajeroViewSet(viewsets.ModelViewSet):
    queryset           = DocumentoPasajero.objects.select_related('pasajero').all()
    serializer_class   = DocumentoPasajeroSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields   = ['pasajero', 'tipo', 'activo']
    search_fields      = ['numero', 'pais_emisor']
    ordering_fields    = ['tipo', 'fecha_vencimiento']
