from .asignacion_tripulacion   import AsignacionTripulacionViewSet
from .checkin                  import CheckInViewSet
from .documento_pasajero       import DocumentoPasajeroViewSet
from .feedback_pasajero        import FeedbackPasajeroViewSet
from .mantenimiento_aeronave   import MantenimientoAeronaveViewSet
from .promocion                import PromocionViewSet
from .solicitud_servicio       import SolicitudServicioViewSet
from .tripulacion              import TripulacionViewSet

__all__ = [
    'AsignacionTripulacionViewSet',
    'CheckInViewSet',
    'DocumentoPasajeroViewSet',
    'FeedbackPasajeroViewSet',
    'MantenimientoAeronaveViewSet',
    'PromocionViewSet',
    'SolicitudServicioViewSet',
    'TripulacionViewSet',
]
