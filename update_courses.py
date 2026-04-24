#!/usr/bin/env python
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorias_project.settings')
django.setup()

from horarios.models import DiaSemana, HorarioTutoria

def update_courses_to_9no_semester():
    print("Actualizando cursos al 9no semestre...")
    
    # Obtener días de la semana
    dias = {
        'Lunes': DiaSemana.objects.get_or_create(nombre='Lunes')[0],
        'Martes': DiaSemana.objects.get_or_create(nombre='Martes')[0],
        'Miércoles': DiaSemana.objects.get_or_create(nombre='Miércoles')[0],
        'Jueves': DiaSemana.objects.get_or_create(nombre='Jueves')[0],
        'Viernes': DiaSemana.objects.get_or_create(nombre='Viernes')[0]
    }
    
    # Eliminar todos los cursos existentes
    print("Eliminando cursos anteriores...")
    HorarioTutoria.objects.all().delete()
    
    # Lista de nuevos cursos del 9no semestre
    # NOTA: Ajusta el paralelo, día y hora según tu horario oficial
    cursos_9no = [
        {
            'materia': 'APLICACION DE MATEMATICAS Y ES',
            'paralelo': '100-ECTS',
            'dia': dias['Lunes'],
            'hora_inicio': '07:00',
            'hora_fin': '09:00',
            'periodo': 'ABR/2026 - AGO/2026'
        },
        {
            'materia': 'EVALUACION DE LA SEGUR EN SIST',
            'paralelo': '100-ECTS',
            'dia': dias['Martes'],
            'hora_inicio': '09:00',
            'hora_fin': '11:00',
            'periodo': 'ABR/2026 - AGO/2026'
        },
        {
            'materia': 'GOBERNANZA DE TECNOL DE INFOR',
            'paralelo': '100-ECTS',
            'dia': dias['Miércoles'],
            'hora_inicio': '11:00',
            'hora_fin': '13:00',
            'periodo': 'ABR/2026 - AGO/2026'
        },
        {
            'materia': 'PRACTICUM III SERVICIO',
            'paralelo': '100-ECTS',
            'dia': dias['Jueves'],
            'hora_inicio': '14:00',
            'hora_fin': '16:00',
            'periodo': 'ABR/2026 - AGO/2026'
        }
    ]
    
    # Crear los nuevos horarios del 9no semestre
    print("Creando cursos del 9no semestre...")
    for curso in cursos_9no:
        horario = HorarioTutoria.objects.create(
            materia=curso['materia'],
            paralelo=curso['paralelo'],
            dia=curso['dia'],
            hora_inicio=curso['hora_inicio'],
            hora_fin=curso['hora_fin'],
            notas=f"Período: {curso['periodo']}"
        )
        print(f"✓ Creado: {horario}")
    
    print(f"\n¡Actualización completada! Se crearon {len(cursos_9no)} cursos del 9no semestre.")

if __name__ == "__main__":
    update_courses_to_9no_semester()
