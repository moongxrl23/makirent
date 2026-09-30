"""Prueba de conexión directa a PostgreSQL, evitando el bug de decodificación
que revienta el traceback de Django. Ejecutar con: python diagnostico_pg.py"""
import psycopg2

try:
    conn = psycopg2.connect(
        dbname="arriendos",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432",
    )
    print("CONEXION OK")
    conn.close()
except Exception as e:
    # Mostramos los bytes crudos del error para evitar el UnicodeDecodeError
    raw = getattr(e, "args", [None])[0]
    print("Tipo de error:", type(e).__name__)
    if isinstance(raw, bytes):
        print("Bytes crudos:", raw)
        print("Como latin-1:", raw.decode("latin-1", errors="replace"))
    else:
        print("Mensaje:", repr(e))
