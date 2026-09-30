"""Carga datos de prueba: python manage.py cargar_datos"""
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from maquinaria.models import Maquina, Cliente, Arriendo


class Command(BaseCommand):
    help = "Crea máquinas, clientes y arriendos de ejemplo"

    def handle(self, *args, **opts):
        if Maquina.objects.exists():
            self.stdout.write("Ya hay datos; no se cargó nada.")
            return
        m = [Maquina.objects.create(**d) for d in [
            dict(nombre="Retroexcavadora CAT 420", categoria="excavacion", precio_dia=180000, descripcion="Ideal para zanjas y movimiento de tierra."),
            dict(nombre="Grúa Horquilla 3 Ton", categoria="elevacion", precio_dia=95000, descripcion="Carga y descarga en bodegas."),
            dict(nombre="Rodillo Compactador", categoria="compactacion", precio_dia=120000, descripcion="Compactación de suelos y asfalto."),
            dict(nombre="Generador 50 kVA", categoria="energia", precio_dia=70000, descripcion="Energía para faenas sin red eléctrica."),
            dict(nombre="Minicargador Bobcat", categoria="excavacion", precio_dia=110000, descripcion="Compacto para espacios reducidos.", disponible=False),
        ]]
        c = [Cliente.objects.create(**d) for d in [
            dict(nombre="Constructora Andes SpA", rut="76.123.456-7", email="contacto@andes.cl", telefono="+56911111111"),
            dict(nombre="Obras Viales del Sur", rut="77.654.321-K", email="obras@viales.cl", telefono="+56922222222"),
            dict(nombre="Juan Pérez", rut="12.345.678-5", email="juan@correo.cl"),
        ]]
        hoy = date.today()
        Arriendo.objects.create(cliente=c[0], maquina=m[0], fecha_inicio=hoy, fecha_fin=hoy + timedelta(days=5))
        Arriendo.objects.create(cliente=c[1], maquina=m[2], fecha_inicio=hoy - timedelta(days=10), fecha_fin=hoy - timedelta(days=3), estado="finalizado")
        Arriendo.objects.create(cliente=c[2], maquina=m[3], fecha_inicio=hoy, fecha_fin=hoy + timedelta(days=2))
        self.stdout.write(self.style.SUCCESS("Datos de prueba cargados."))
