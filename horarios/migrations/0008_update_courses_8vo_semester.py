from django.db import migrations
from django.utils import timezone

def update_courses_to_8vo_semester(apps, schema_editor):
    DiaSemana = apps.get_model('horarios', 'DiaSemana')
    HorarioTutoria = apps.get_model('horarios', 'HorarioTutoria')
    
    # Obtener días de la semana
    dias = {
        'Lunes': DiaSemana.objects.get_or_create(nombre='Lunes')[0],
        'Martes': DiaSemana.objects.get_or_create(nombre='Martes')[0],
        'Miércoles': DiaSemana.objects.get_or_create(nombre='Miércoles')[0],
        'Jueves': DiaSemana.objects.get_or_create(nombre='Jueves')[0],
        'Viernes': DiaSemana.objects.get_or_create(nombre='Viernes')[0]
    }
    
    # Eliminar todos los cursos existentes del 7mo semestre
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
    for curso in cursos_8vo:
        HorarioTutoria.objects.create(
            materia=curso['materia'],
            paralelo=curso['paralelo'],
            dia=curso['dia'],
            hora_inicio=curso['hora_inicio'],
            hora_fin=curso['hora_fin'],
            notas=f"Período: {curso['periodo']}"
        )

def revert_to_7mo_semester(apps, schema_editor):
    DiaSemana = apps.get_model('horarios', 'DiaSemana')
    HorarioTutoria = apps.get_model('horarios', 'HorarioTutoria')
    
    # Obtener días de la semana
    dias = {
        'Lunes': DiaSemana.objects.get_or_create(nombre='Lunes')[0],
        'Martes': DiaSemana.objects.get_or_create(nombre='Martes')[0],
        'Miércoles': DiaSemana.objects.get_or_create(nombre='Miércoles')[0],
        'Jueves': DiaSemana.objects.get_or_create(nombre='Jueves')[0],
        'Viernes': DiaSemana.objects.get_or_create(nombre='Viernes')[0]
    }
    
    # Eliminar todos los cursos del 8vo semestre
    HorarioTutoria.objects.all().delete()
    
    # Restaurar cursos del 7mo semestre
    cursos_7mo = [
        {
            'materia': 'ARQUITECTURA DE REDES',
            'paralelo': '100-ECTS-RED',
            'dia': dias['Lunes'],
            'hora_inicio': '07:00',
            'hora_fin': '09:00',
            'periodo': 'ABR/2025 - AGO/2025'
        },
        {
            'materia': 'ARQUITECTURA DE SOFTWARE',
            'paralelo': '100-ECTS-RED',
            'dia': dias['Martes'],
            'hora_inicio': '09:00',
            'hora_fin': '11:00',
            'periodo': 'ABR/2025 - AGO/2025'
        },
        {
            'materia': 'ARQUITECTURA EMPRESARIAL',
            'paralelo': '100-ECTS-RED',
            'dia': dias['Miércoles'],
            'hora_inicio': '11:00',
            'hora_fin': '13:00',
            'periodo': 'ABR/2025 - AGO/2025'
        },
        {
            'materia': 'CONSEJERO ESTUDIANTIL TECNOLOGIAS DE LA INFORMACION (EN LINEA)',
            'paralelo': '100-ECTS-RED',
            'dia': dias['Jueves'],
            'hora_inicio': '14:00',
            'hora_fin': '16:00',
            'periodo': 'ABR/2025 - AGO/2025'
        },
        {
            'materia': 'DESARROLLO BASADO EN PLATAF MO',
            'paralelo': '100-ECTS-RED',
            'dia': dias['Viernes'],
            'hora_inicio': '16:00',
            'hora_fin': '18:00',
            'periodo': 'ABR/2025 - AGO/2025'
        },
        {
            'materia': 'GESTION DE PROYECTOS',
            'paralelo': '100-ECTS-RED',
            'dia': dias['Lunes'],
            'hora_inicio': '18:00',
            'hora_fin': '20:00',
            'periodo': 'ABR/2025 - AGO/2025'
        }
    ]
    
    # Crear los horarios del 7mo semestre
    for curso in cursos_7mo:
        HorarioTutoria.objects.create(
            materia=curso['materia'],
            paralelo=curso['paralelo'],
            dia=curso['dia'],
            hora_inicio=curso['hora_inicio'],
            hora_fin=curso['hora_fin'],
            notas=f"Período: {curso['periodo']}"
        )

class Migration(migrations.Migration):
    dependencies = [
        ('horarios', '0007_comentariohorario'),
    ]

    operations = [
        migrations.RunPython(update_courses_to_8vo_semester, revert_to_7mo_semester),
    ]

