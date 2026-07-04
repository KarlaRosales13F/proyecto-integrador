from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from vuelos.models import Equipaje
from vuelos.serializers import EquipajeSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura

class EquipajeViewSet(viewsets.ModelViewSet):
    queryset           = Equipaje.objects.select_related('reserva').all()
    serializer_class   = EquipajeSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields   = ['tipo', 'reserva']
    ordering_fields    = ['tipo', 'peso_kg']
