from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from vuelos.models import FeedbackPasajero
from vuelos.serializers import FeedbackPasajeroSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura

class FeedbackPasajeroViewSet(viewsets.ModelViewSet):
    queryset           = FeedbackPasajero.objects.select_related('reserva').all()
    serializer_class   = FeedbackPasajeroSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields   = ['reserva', 'calificacion']
    search_fields      = ['comentario']
    ordering_fields    = ['calificacion', 'fecha_feedback']
