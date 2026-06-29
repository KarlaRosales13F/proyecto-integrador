# Avianco — Sistema de Gestión de Aerolínea

API REST desarrollada con Django y Django REST Framework para gestionar de forma integral los procesos de una aerolínea: vuelos, reservas, pasajeros, pagos, aeropuertos, aeronaves y configuraciones operativas.

---

## Información General

| Campo | Descripción |
|---|---|
| Nombre del proyecto | Avianco — Sistema de Gestión de Aerolínea (Backend API) |
| Integrantes | Jossue Guerrero, Aliyha Mazsorra, Karla Rosales |
| Descripción | API RESTful para administrar vuelos, reservas, pasajeros, pagos y datos operativos del negocio aéreo. |
| Autenticación | JWT (JSON Web Tokens) |
| Acceso | Lectura para usuarios autenticados y escritura para usuarios con permisos de staff |

## Descripción del Sistema

Avianco permite centralizar la lógica de negocio de una aerolínea a través de recursos API para:

- Gestión de vuelos, aeropuertos, aeronaves y rutas.
- Registro y seguimiento de reservas y pasajeros.
- Gestión de pagos, métodos de pago, tarifas y servicios auxiliares.
- Administración de datos operativos como terminales, puertas, escalas, estados de vuelo y notificaciones.
- Control de acceso mediante autenticación JWT.

## Modelos Principales

El sistema contempla 25 entidades del dominio para cubrir la operación completa de una aerolínea:

| Modelo | Función principal |
|---|---|
| Aeronave | Representa las aeronaves disponibles para los vuelos. |
| Aeropuerto | Almacena los aeropuertos de origen y destino. |
| Terminal | Organiza las terminales internas de un aeropuerto. |
| Puerta | Registra las puertas asociadas a cada terminal. |
| País | Contiene los países relacionados con aeropuertos y ubicaciones. |
| Ciudad | Guarda las ciudades asociadas a los países. |
| Pasajero | Mantiene los datos del usuario viajero. |
| Vuelo | Define los viajes, horarios, estados y precio. |
| Reserva | Registra la reserva de un pasajero en un vuelo. |
| EstadoVuelo | Representa los estados operativos del vuelo. |
| Escala | Gestiona las escalas intermedias de un viaje. |
| TipoAvion | Clasifica las aeronaves por tipo. |
| Tarifa | Define los costos asociados a rutas o servicios. |
| Equipaje | Registra el equipaje de los pasajeros. |
| MetodoPago | Clasifica los métodos de pago disponibles. |
| Pago | Gestiona los pagos realizados por los pasajeros. |
| Notificacion | Envía mensajes o alertas al usuario. |
| Tripulacion | Almacena los miembros del personal de vuelo. |
| AsignacionTripulacion | Relaciona tripulación con vuelos específicos. |
| CheckIn | Registra el proceso de check-in de una reserva. |
| DocumentoPasajero | Guarda documentos oficiales del pasajero. |
| FeedbackPasajero | Permite registrar opiniones y calificaciones. |
| MantenimientoAeronave | Controla los mantenimientos de la aeronave. |
| Promocion | Administra códigos y descuentos vigentes. |
| SolicitudServicio | Registra solicitudes especiales de pasajeros. |

## Tecnologías

| Tecnología | Versión / Uso |
|---|---|
| Python | 3.13 |
| Django | 6.0 |
| Django REST Framework | 3.17+ |
| PostgreSQL | Base de datos principal |
| SimpleJWT | Autenticación con JWT |
| Gunicorn | Servidor WSGI para producción |
| Nginx | Proxy inverso y despliegue |
| django-filter | Filtros de consulta |
| django-cors-headers | Soporte CORS |

## Instalación

### Clonar el repositorio

```bash
git clone https://github.com/KarlaRosales13F/proyecto-integrador.git
cd proyecto-integrador
```

### Crear el entorno virtual

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto con contenido similar a:

```env
DEBUG=True
DB_NAME=sistema_vuelos
DB_USER=sistema_vuelos
DB_PASSWORD=sistema_vuelos
DB_HOST=localhost
DB_PORT=5432
```

### Ejecutar migraciones

```bash
python manage.py migrate
```

### Crear un superusuario

```bash
python manage.py createsuperuser
```

### Ejecutar el servidor

```bash
python manage.py runserver
```

## Despliegue

Para producción se recomienda:

- Configurar un VPS con Python, PostgreSQL y firewall.
- Instalar PostgreSQL y preparar la base de datos para producción.
- Ejecutar la aplicación con Gunicorn.
- Configurar Nginx como proxy inverso.
- Usar `DEBUG=False` y variables seguras de entorno.

## Uso de la API

La API utiliza JWT para proteger los endpoints. Para autenticarse, se obtiene un token y se envía en el encabezado `Authorization`.


### Permisos

| Tipo de usuario | Permisos |
|---|---|
| No autenticado | Sin acceso |
| Autenticado | Lectura de recursos |
| Staff | Lectura y escritura completa |


## Endpoints Principales

Rutas disponibles del backend, agrupadas por módulo:

| Módulo | Rutas principales |
|---|---|
| Autenticación | `/api/token/`, `/api/token/refresh/` |
| Aeronaves | `/api/aeronaves/` |
| Aeropuertos | `/api/aeropuertos/` |
| Países y ciudades | `/api/paises/`, `/api/ciudades/` |
| Terminales y puertas | `/api/terminales/`, `/api/puertas/` |
| Pasajeros | `/api/pasajeros/` |
| Vuelos | `/api/vuelos/` |
| Reservas | `/api/reservas/` |
| Tipos de avión | `/api/tipos-avion/` |
| Tarifas | `/api/tarifas/` |
| Equipajes | `/api/equipajes/` |
| Escalas | `/api/escalas/` |
| Estados de vuelo | `/api/estados-vuelo/` |
| Métodos de pago | `/api/metodos-pago/` |
| Notificaciones | `/api/notificaciones/` |
| Pagos | `/api/pagos/` |
| Administración | `/admin/` |

## Estructura del Proyecto

```text
proyecto-integrador/
├── avianco/
│   ├── models/
│   ├── serializers/
│   ├── views/
│   ├── migrations/
│   └── tests.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

*Proyecto Integrador — Desarrollo de APIs con Django REST Framework*
