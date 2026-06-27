from .asignacion_tripulacion   import AsignacionTripulacionSerializer
from .checkin                  import CheckInSerializer
from .documento_pasajero       import DocumentoPasajeroSerializer
from .feedback_pasajero        import FeedbackPasajeroSerializer
from .mantenimiento_aeronave   import MantenimientoAeronaveSerializer
from .promocion                import PromocionSerializer
from .solicitud_servicio       import SolicitudServicioSerializer
from .tripulacion              import TripulacionSerializer

__all__ = [
    'AsignacionTripulacionSerializer',
    'CheckInSerializer',
    'DocumentoPasajeroSerializer',
    'FeedbackPasajeroSerializer',
    'MantenimientoAeronaveSerializer',
    'PromocionSerializer',
    'SolicitudServicioSerializer',
    'TripulacionSerializer',
]
