from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from vuelos.models import Pago
from vuelos.serializers import PagoSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura

class PagoViewSet(viewsets.ModelViewSet):
    queryset           = Pago.objects.select_related('reserva', 'metodo_pago').all()
    serializer_class   = PagoSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, OrderingFilter]
    filterset_fields   = ['reserva', 'metodo_pago', 'estado']
    ordering_fields    = ['-fecha']
