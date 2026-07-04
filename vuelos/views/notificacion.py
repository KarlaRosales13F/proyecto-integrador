from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from vuelos.models import Notificacion
from vuelos.serializers import NotificacionSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura

class NotificacionViewSet(viewsets.ModelViewSet):
    queryset           = Notificacion.objects.select_related('usuario').all()
    serializer_class   = NotificacionSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, OrderingFilter]
    filterset_fields   = ['usuario', 'tipo', 'leida']
    ordering_fields    = ['-fecha']
