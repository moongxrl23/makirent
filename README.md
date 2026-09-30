# MaquiRent – Arriendo de maquinaria (Django + DRF + PostgreSQL)

## Requisitos
- Python 3.x
- Docker Desktop (abierto y corriendo)

## Pasos, en orden

### 1. Abrir la carpeta en una terminal
En Visual Studio Code: abre la carpeta del proyecto y abre una terminal (Terminal > Nueva terminal).
Debe quedar posicionada donde está `manage.py` (junto a `docker-compose.yml`).

### 2. Levantar PostgreSQL con Docker
```
docker compose up -d
```
Verifica que quedó corriendo:
```
docker ps
```
Debe aparecer un contenedor con imagen `postgres:16` y estado "Up".

### 3. Instalar dependencias de Python
```
pip install -r requirements.txt
```

### 4. Verificar la conexión (opcional pero recomendado)
```
python diagnostico_pg.py
```
Debe imprimir `CONEXION OK`. Si no, revisa la sección "Problemas comunes" más abajo.

### 5. Crear las tablas y cargar datos de prueba
```
python manage.py makemigrations maquinaria
python manage.py migrate
python manage.py cargar_datos
```

### 6. Levantar el servidor
```
python manage.py runserver
```
Abre en el navegador: http://127.0.0.1:8000/

Páginas: `/`, `/maquinas/`, `/clientes/`, `/arriendos/`, `/contacto/` · API: `/api/`

Para ver el 404 personalizado (Django lo oculta si `DEBUG=True`):
```
$env:DEBUG="False"; python manage.py runserver
```
y visita cualquier URL que no exista, ej: http://127.0.0.1:8000/algo-que-no-existe/

## Problemas comunes

**"docker: command not found" o similar**
Docker Desktop no está abierto, o no terminó de iniciar. Ábrelo y espera a que la ballena del ícono deje de animarse.

**`diagnostico_pg.py` muestra un error de autenticación**
Puede haber otro PostgreSQL instalado en el PC (no debería pasar en uno limpio, pero si instalaste
PostgreSQL por fuera de Docker en algún momento, revisa `Get-Service *postgres*` en PowerSHell
y detén ese servicio: `Stop-Service nombre-del-servicio` en una PowerShell como Administrador).

**Quiero borrar todo y empezar de cero con la base de datos**
```
docker compose down -v
docker compose up -d
```
(el `-v` borra también los datos guardados; útil si algo quedó mal configurado)
