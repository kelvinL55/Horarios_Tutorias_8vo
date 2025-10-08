#!/usr/bin/env python
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorias_project.settings')
django.setup()

from horarios.models import DiaSemana, HorarioTutoria

def update_courses_to_8vo_semester():
    print("Actualizando cursos al 8vo semestre...")
    
    # Obtener días de la semana
    dias = {
        'Lunes': DiaSemana.objects.get_or_create(nombre='Lunes')[0],
        'Martes': DiaSemana.objects.get_or_create(nombre='Martes')[0],
        'Miércoles': DiaSemana.objects.get_or_create(nombre='Miércoles')[0],
        'Jueves': DiaSemana.objects.get_or_create(nombre='Jueves')[0],
        'Viernes': DiaSemana.objects.get_or_create(nombre='Viernes')[0]
    }
    
    # Eliminar todos los cursos existentes del 7mo semestre
    print("Eliminando cursos del 7mo semestre...")
    HorarioTutoria.objects.all().delete()
    
    # Lista de nuevos cursos del 8vo semestre
    cursos_8vo = [
        {
            'materia': 'FUNDAMENTOS Y APLICACION DE SE',
            'paralelo': '100-ECTS-RED',
            'dia': dias['Lunes'],
            'hora_inicio': '07:00',
            'hora_fin': '09:00',
            'periodo': 'OCT/2025 - FEB/2026'
        },
        {
            'materia': 'ORGANIZACION Y ADMIN DE INFRAE',
            'paralelo': '100-ECTS-RED',
            'dia': dias['Martes'],
            'hora_inicio': '09:00',
            'hora_fin': '11:00',
            'periodo': 'OCT/2025 - FEB/2026'
        },
        {
            'materia': 'PRACTICUM II',
            'paralelo': '100-ECTS-RED',
            'dia': dias['Miércoles'],
            'hora_inicio': '11:00',
            'hora_fin': '13:00',
            'periodo': 'OCT/2025 - FEB/2026'
        },
        {
            'materia': 'PROGRAMACION INTEGRATIVA',
            'paralelo': '100-ECTS-RED',
            'dia': dias['Jueves'],
            'hora_inicio': '14:00',
            'hora_fin': '16:00',
            'periodo': 'OCT/2025 - FEB/2026'
        },
        {
            'materia': 'SISTEMAS DISTRIBUIDOS',
            'paralelo': '100-ECTS-RED',
            'dia': dias['Viernes'],
            'hora_inicio': '16:00',
            'hora_fin': '18:00',
            'periodo': 'OCT/2025 - FEB/2026'
        }
    ]
    
    # Crear los nuevos horarios del 8vo semestre
    print("Creando cursos del 8vo semestre...")
    for curso in cursos_8vo:
        horario = HorarioTutoria.objects.create(
            materia=curso['materia'],
            paralelo=curso['paralelo'],
            dia=curso['dia'],
            hora_inicio=curso['hora_inicio'],
            hora_fin=curso['hora_fin'],
            notas=f"Período: {curso['periodo']}"
        )
        print(f"✓ Creado: {horario}")
    
    print(f"\n¡Actualización completada! Se crearon {len(cursos_8vo)} cursos del 8vo semestre.")

if __name__ == "__main__":
    update_courses_to_8vo_semester()

