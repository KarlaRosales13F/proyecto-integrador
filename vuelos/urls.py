from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from vuelos.views.health              import health_check
from vuelos.views.auth                import RegisterView, LogoutView
from vuelos.views.user                import UserViewSet
from vuelos.views.aeropuerto          import AeropuertoViewSet
from vuelos.views.aeronave            import AeronaveViewSet
from vuelos.views.vuelo               import VueloViewSet
from vuelos.views.pasajero            import PasajeroViewSet
from vuelos.views.reserva             import ReservaViewSet
from vuelos.views.pais                import PaisViewSet
from vuelos.views.ciudad              import CiudadViewSet
from vuelos.views.terminal            import TerminalViewSet
from vuelos.views.puerta              import PuertaViewSet
from vuelos.views.tipo_avion          import TipoAvionViewSet
from vuelos.views.tarifa              import TarifaViewSet
from vuelos.views.equipaje            import EquipajeViewSet
from vuelos.views.tripulacion         import TripulacionViewSet
from vuelos.views.asignacion_tripulacion import AsignacionTripulacionViewSet
from vuelos.views.escala              import EscalaViewSet
from vuelos.views.estado_vuelo        import EstadoVueloViewSet
from vuelos.views.notificacion        import NotificacionViewSet
from vuelos.views.metodo_pago         import MetodoPagoViewSet
from vuelos.views.pago                import PagoViewSet
from vuelos.views.promocion           import PromocionViewSet
from vuelos.views.aerolinea           import AerolineaViewSet
from vuelos.views.asiento             import AsientoViewSet
from vuelos.views.checkin             import CheckInViewSet
from vuelos.views.servicio            import ServicioViewSet, ReservaServicioViewSet
from vuelos.views.factura             import FacturaViewSet
from vuelos.serializers.auth          import CustomTokenView

router = DefaultRouter()
router.register('usuarios',              UserViewSet,                  basename='usuario')
router.register('aeropuertos',           AeropuertoViewSet,            basename='aeropuerto')
router.register('aeronaves',             AeronaveViewSet,              basename='aeronave')
router.register('vuelos',               VueloViewSet,                 basename='vuelo')
router.register('pasajeros',            PasajeroViewSet,              basename='pasajero')
router.register('reservas',             ReservaViewSet,               basename='reserva')
router.register('paises',               PaisViewSet,                  basename='pais')
router.register('ciudades',             CiudadViewSet,                basename='ciudad')
router.register('terminales',           TerminalViewSet,              basename='terminal')
router.register('puertas',              PuertaViewSet,                basename='puerta')
router.register('tipos-avion',          TipoAvionViewSet,             basename='tipo-avion')
router.register('tarifas',              TarifaViewSet,                basename='tarifa')
router.register('equipajes',            EquipajeViewSet,              basename='equipaje')
router.register('tripulacion',          TripulacionViewSet,           basename='tripulacion')
router.register('asignaciones',         AsignacionTripulacionViewSet, basename='asignacion')
router.register('escalas',              EscalaViewSet,                basename='escala')
router.register('estados-vuelo',        EstadoVueloViewSet,           basename='estado-vuelo')
router.register('notificaciones',       NotificacionViewSet,          basename='notificacion')
router.register('metodos-pago',         MetodoPagoViewSet,            basename='metodo-pago')
router.register('pagos',                PagoViewSet,                  basename='pago')
router.register('promociones',          PromocionViewSet,             basename='promocion')
router.register('aerolineas',           AerolineaViewSet,             basename='aerolinea')
router.register('asientos',             AsientoViewSet,               basename='asiento')
router.register('checkins',             CheckInViewSet,               basename='checkin')
router.register('servicios',            ServicioViewSet,              basename='servicio')
router.register('reserva-servicios',    ReservaServicioViewSet,       basename='reserva-servicio')
router.register('facturas',             FacturaViewSet,               basename='factura')

urlpatterns = [
    path('health/',             health_check),
    path('auth/registro/',      RegisterView.as_view()),
    path('auth/login/',         CustomTokenView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('auth/token/verify/',  TokenVerifyView.as_view()),
    path('auth/logout/',        LogoutView.as_view()),
    path('', include(router.urls)),
]