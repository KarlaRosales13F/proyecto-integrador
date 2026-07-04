from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from vuelos.models import Factura
from vuelos.serializers.factura import FacturaSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura


class FacturaViewSet(viewsets.ModelViewSet):
    queryset           = Factura.objects.select_related('reserva').all()
    serializer_class   = FacturaSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, OrderingFilter]
    filterset_fields   = ['estado', 'reserva']
    ordering_fields    = ['-fecha']
