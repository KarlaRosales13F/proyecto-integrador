from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from vuelos.models import Reserva
from vuelos.serializers import ReservaSerializer
from vuelos.pagination import StandardPagination
from vuelos.filters import ReservaFilter


class ReservaViewSet(viewsets.ModelViewSet):
    queryset           = Reserva.objects.select_related('vuelo', 'pasajero').all()
    serializer_class   = ReservaSerializer
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class    = ReservaFilter
    ordering_fields    = ['fecha_reserva', 'estado']

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'create']:
            return [IsAuthenticated()]
        return [IsAdminUser()]

    @action(detail=True, methods=['post'],
            permission_classes=[IsAuthenticated], url_path='cancelar')
    def cancelar(self, request, pk=None):
        reserva = self.get_object()
        if reserva.estado == 'cancelada':
            return Response(
                {'error': 'La reserva ya está cancelada.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        reserva.estado = 'cancelada'
        reserva.save(update_fields=['estado'])
        return Response({'mensaje': 'Reserva cancelada.', 'estado': reserva.estado})

    @action(detail=False, methods=['get'], url_path='estadisticas')
    def estadisticas(self, request):
        qs = Reserva.objects.all()
        return Response({
            'total':       qs.count(),
            'confirmadas': qs.filter(estado='confirmada').count(),
            'canceladas':  qs.filter(estado='cancelada').count(),
            'embarcados':  qs.filter(estado='embarcado').count(),
        })