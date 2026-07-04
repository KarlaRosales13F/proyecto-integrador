from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from vuelos.models import Escala
from vuelos.serializers import EscalaSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura

class EscalaViewSet(viewsets.ModelViewSet):
    queryset           = Escala.objects.select_related('vuelo', 'aeropuerto').all()
    serializer_class   = EscalaSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, OrderingFilter]
    filterset_fields   = ['vuelo', 'aeropuerto']
    ordering_fields    = ['orden', 'llegada']
