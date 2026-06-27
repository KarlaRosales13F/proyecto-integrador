from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from vuelos.models import Promocion
from vuelos.serializers import PromocionSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura

class PromocionViewSet(viewsets.ModelViewSet):
    queryset           = Promocion.objects.all()
    serializer_class   = PromocionSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields   = ['activa']
    search_fields      = ['codigo', 'descripcion']
    ordering_fields    = ['codigo', 'fecha_inicio', 'descuento']
