from django.db import models

class Disciplina(models.Model):
  nombre = models.CharField(max_length=30)

class Participante(models.Model):
  nombres = models.CharField(max_length=255)
  apellido_paterno = models.CharField(max_length=255)
  apellido_materno = models.CharField(max_length=255)
  estado = models.BooleanField(default=True)
  ultima_comida = models.BooleanField(default=False)
  institucion = models.CharField(max_length=255)
  TIPOS_CHOICES = (
    ('deportista', 'DEPORTISTA'),
    ('entrenador', 'ENTRENADOR'),
    ('juez', 'JUEZ'),
    ('delegado', 'DELEGADO'),
    ('coordinador', 'COORDINADOR'),
    ('comisionado-tecnico', 'COMISIONADO TÉCNICO'),
    ('medico', 'MÉDICO'),
    ('comite-organizador', 'COMITÉ ORGANIZADOR'),
  )
  tipos = models.CharField(
    max_length=19,
    choices=TIPOS_CHOICES,
    default='deportista'
  )

  