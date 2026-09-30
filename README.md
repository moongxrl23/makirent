# MakiRent - Sistema de arriendo de maquinaria

Proyecto para el ramo de Backend (INACAP). Sistema web para arrendar maquinaria pesada (excavadoras, grúas, compactadores, generadores), hecho con Django y Django REST Framework.

## Cómo levantarlo

Necesitas tener Docker Desktop abierto y Python instalado.

Levantar la base de datos:

docker compose up -d


Instalar las librerías:

pip install -r requirements.txt


Crear las tablas y cargar datos de prueba:

python manage.py makemigrations maquinaria
python manage.py migrate
python manage.py cargar_datos


Correr el servidor:

python manage.py runserver


Y entrar a http://127.0.0.1:8000/

## Qué tiene

- Landing page, catálogo de máquinas, clientes y arriendos, todo con templates (sin usar el admin de Django)
- Se puede crear, editar y eliminar máquinas, clientes y arriendos
- Página de error 404 personalizada
- API REST en /api/
- Base de datos en PostgreSQL (corriendo en un contenedor Docker)
- Datos de prueba precargados

## Estructura

- `maquinaria/models.py` - los modelos (Maquina, Cliente, Arriendo)
- `maquinaria/views.py` - las vistas
- `maquinaria/templates/` - los HTML
- `maquinaria/static/` - CSS e imágenes

Nombre: Valentina Alvarado
Carrera: Analista Programador - INACAP