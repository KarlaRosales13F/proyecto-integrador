from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from vuelos.models import Servicio, ReservaServicio
from vuelos.serializers.servicio import ServicioSerializer, ReservaServicioSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura


class ServicioViewSet(viewsets.ModelViewSet):
    queryset           = Servicio.objects.all()
    serializer_class   = ServicioSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields   = ['tipo']
    search_fields      = ['nombre', 'tipo']
    ordering_fields    = ['nombre', 'precio']


class ReservaServicioViewSet(viewsets.ModelViewSet):
    queryset           = ReservaServicio.objects.select_related('reserva', 'servicio').all()
    serializer_class   = ReservaServicioSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, OrderingFilter]
    filterset_fields   = ['reserva', 'servicio']
