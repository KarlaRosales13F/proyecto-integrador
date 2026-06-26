from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from vuelos.models import MetodoPago
from vuelos.serializers import MetodoPagoSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura

class MetodoPagoViewSet(viewsets.ModelViewSet):
    queryset           = MetodoPago.objects.all()
    serializer_class   = MetodoPagoSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields   = ['tipo', 'activo']
    search_fields      = ['nombre', 'tipo']
    ordering_fields    = ['nombre', 'tipo']
