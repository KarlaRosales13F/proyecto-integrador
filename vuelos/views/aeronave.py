from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from vuelos.models import Aeronave
from vuelos.serializers import AeronaveSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura
from vuelos.filters import AeronaveFilter


class AeronaveViewSet(viewsets.ModelViewSet):
    queryset           = Aeronave.objects.all()
    serializer_class   = AeronaveSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class    = AeronaveFilter
    search_fields      = ['matricula', 'modelo']
    ordering_fields    = ['modelo', 'capacidad']

    @action(detail=False, methods=['get'], url_path='estadisticas')
    def estadisticas(self, request):
        from django.db.models import Avg, Max, Min
        qs = Aeronave.objects.all()
        return Response({
            'total':            qs.count(),
            'capacidad_promedio': round(qs.aggregate(Avg('capacidad'))['capacidad__avg'] or 0, 0),
            'capacidad_maxima':  qs.aggregate(Max('capacidad'))['capacidad__max'],
            'capacidad_minima':  qs.aggregate(Min('capacidad'))['capacidad__min'],
        })