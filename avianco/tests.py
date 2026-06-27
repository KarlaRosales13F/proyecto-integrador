from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

# Create your tests here.

from vuelos.views.equipaje            import EquipajeViewSet
from vuelos.views.escala              import EscalaViewSet
from vuelos.views.estado_vuelo        import EstadoVueloViewSet
from vuelos.views.metodo_pago         import MetodoPagoViewSet
from vuelos.views.pago                import PagoViewSet
from vuelos.views.tarifa              import TarifaViewSet
from vuelos.views.tipo_avion          import TipoAvionViewSet
from vuelos.views.notificacion        import NotificacionViewSet


router.register('tipos-avion',          TipoAvionViewSet,             basename='tipo-avion')
router.register('tarifas',              TarifaViewSet,                basename='tarifa')
router.register('equipajes',            EquipajeViewSet,              basename='equipaje')
router.register('escalas',              EscalaViewSet,                basename='escala')
router.register('estados-vuelo',        EstadoVueloViewSet,           basename='estado-vuelo')
router.register('metodos-pago',         MetodoPagoViewSet,            basename='metodo-pago')
router.register('notificaciones',       NotificacionViewSet,          basename='notificacion')
router.register('pagos',                PagoViewSet,                  basename='pago')

