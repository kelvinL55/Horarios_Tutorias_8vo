from django.core.management.base import BaseCommand
from horarios.models import DiaSemana, HorarioTutoria
from datetime import time

class Command(BaseCommand):
    help = 'Actualiza los cursos del 7mo semestre al 8vo semestre'

    def handle(self, *args, **options):
        self.stdout.write("Actualizando cursos al 8vo semestre...")
        
        # Obtener días de la semana
        dias = {
            'Lunes': DiaSemana.objects.get_or_create(nombre='Lunes')[0],
            'Martes': DiaSemana.objects.get_or_create(nombre='Martes')[0],
            'Miércoles': DiaSemana.objects.get_or_create(nombre='Miércoles')[0],
            'Jueves': DiaSemana.objects.get_or_create(nombre='Jueves')[0],
            'Viernes': DiaSemana.objects.get_or_create(nombre='Viernes')[0]
        }
        
        # Eliminar todos los cursos existentes del 7mo semestre
        self.stdout.write("Eliminando cursos del 7mo semestre...")
        HorarioTutoria.objects.all().delete()
        
        # Lista de nuevos cursos del 8vo semestre
        cursos_8vo = [
            {
                'materia': 'Fundamentos y Aplicacion de SE',
                'paralelo': '100-ECTS-RED',
                'dia': dias['Lunes'],
                'hora_inicio': time(7, 0),
                'hora_fin': time(9, 0),
                'periodo': 'OCT/2025 - FEB/2026'
            },
            {
                'materia': 'Organizacion y Admin de Infrae',
                'paralelo': '100-ECTS-RED',
                'dia': dias['Martes'],
                'hora_inicio': time(9, 0),
                'hora_fin': time(11, 0),
                'periodo': 'OCT/2025 - FEB/2026'
            },
            {
                'materia': 'Practicum II',
                'paralelo': '100-ECTS-RED',
                'dia': dias['Miércoles'],
                'hora_inicio': time(11, 0),
                'hora_fin': time(13, 0),
                'periodo': 'OCT/2025 - FEB/2026'
            },
            {
                'materia': 'Programacion Integrativa',
                'paralelo': '100-ECTS-RED',
                'dia': dias['Jueves'],
                'hora_inicio': time(14, 0),
                'hora_fin': time(16, 0),
                'periodo': 'OCT/2025 - FEB/2026'
            },
            {
                'materia': 'Sistemas Distribuidos',
                'paralelo': '100-ECTS-RED',
                'dia': dias['Viernes'],
                'hora_inicio': time(16, 0),
                'hora_fin': time(18, 0),
                'periodo': 'OCT/2025 - FEB/2026'
            }
        ]
        
        # Crear los nuevos horarios del 8vo semestre
        self.stdout.write("Creando cursos del 8vo semestre...")
        for curso in cursos_8vo:
            horario = HorarioTutoria.objects.create(
                materia=curso['materia'],
                paralelo=curso['paralelo'],
                dia=curso['dia'],
                hora_inicio=curso['hora_inicio'],
                hora_fin=curso['hora_fin'],
                notas=f"Período: {curso['periodo']}"
            )
            self.stdout.write(f"Creado: {horario}")
        
        self.stdout.write(
            self.style.SUCCESS(f"\n¡Actualización completada! Se crearon {len(cursos_8vo)} cursos del 8vo semestre.")
        )

