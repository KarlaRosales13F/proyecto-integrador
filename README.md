# Sistema de Vuelos - Backend API

API REST desarrollada con Django y Django REST Framework para la gestión de vuelos, reservas y pasajeros.

## Tecnologías

- Python 3.13
- Django 6.0
- Django REST Framework
- PostgreSQL
- JWT Authentication

## Instalación

Clonar el repositorio y crear el entorno virtual:

```bash
git clone https://github.com/JossGuerrero/sistema-vuelos.git
cd sistema-vuelos
uv sync
```

Configurar variables de entorno en `.env`:

DEBUG=True
DB_NAME=sistema_vuelos
DB_USER=sistema_vuelos
DB_PASSWORD=sistema_vuelos
DB_HOST=localhost
DB_PORT=5432

Aplicar migraciones y correr el servidor:

```bash
uv run python manage.py migrate
uv run python manage.py runserver
```

## Endpoints principales

- `POST /api/auth/login/` — iniciar sesión
- `POST /api/auth/registro/` — registrar usuario
- `GET /api/vuelos/` — listar vuelos
- `GET /api/aeropuertos/` — listar aeropuertos
- `GET /api/reservas/` — listar reservas
- `GET /api/pasajeros/` — listar pasajeros
- `GET /api/aeronaves/` — listar aeronaves

## Autenticación

La API usa JWT. Para acceder a los endpoints protegidos hay que incluir el token en el header: