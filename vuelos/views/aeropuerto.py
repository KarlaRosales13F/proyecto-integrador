from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count

from vuelos.models import Aeropuerto
from vuelos.serializers import AeropuertoSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura
from vuelos.filters import AeropuertoFilter


class AeropuertoViewSet(viewsets.ModelViewSet):
    queryset           = Aeropuerto.objects.all()
    serializer_class   = AeropuertoSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class    = AeropuertoFilter
    search_fields      = ['codigo_iata', 'nombre', 'ciudad', 'pais']
    ordering_fields    = ['codigo_iata', 'pais', 'ciudad']

    @action(detail=False, methods=['get'], url_path='estadisticas')
    def estadisticas(self, request):
        qs = Aeropuerto.objects.all()
        return Response({
            'total':    qs.count(),
            'por_pais': list(qs.values('pais').annotate(total=Count('id')).order_by('-total')),
        })