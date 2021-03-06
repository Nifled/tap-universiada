import uuid
from django.db import models
from random import randint

from .choices import *
from . import barcodes


# ----------------------------------------------------------------------
# **************************** Disciplina ******************************
# ----------------------------------------------------------------------
class Disciplina(models.Model):
    nombre = models.CharField(max_length=85)

    def __str__(self):
        return self.nombre


# ----------------------------------------------------------------------
# *************************** Participante *****************************
# ----------------------------------------------------------------------
class Participante(models.Model):
    uuid = models.UUIDField(blank=True, default=uuid.uuid4, editable=False, unique=True)
    barcode = models.CharField(max_length=13, blank=True, editable=False, unique=True)
    barcode_link = models.CharField(max_length=35, blank=True, editable=False, unique=True)
    nombres = models.CharField(max_length=85)
    apellido_p = models.CharField(max_length=45, verbose_name='Apellido Paterno')
    apellido_m = models.CharField(max_length=45, verbose_name='Apellido Materno')
    estatus = models.BooleanField(default=True, editable=False)  # True = en competencia, False = eliminado
    institucion = models.CharField(max_length=85)
    tipo = models.IntegerField(choices=PARTICIPANTE_TIPOS)  # Choices en ./choices.py

    # `estatos` == False (eliminado) y `ultima_comida` == True, ya no puede comer nunca.
    ultima_comida = models.BooleanField(default=False, editable=False)
    datetime_eliminacion = models.DateTimeField(editable=False, blank=True, null=True)

    # Foreign Keys
    disciplina = models.ForeignKey(Disciplina, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{} - {}, Estatus: {} {}'\
            .format(self.apellido_p, self.disciplina.nombre, self.estatus, self.get_tipo_display())

    def save(self, *args, **kwargs):
        barcode_str, barcode_link = barcodes.generate_one(str(randint(100000000000, 999999999999)))
        self.barcode = barcode_str
        self.barcode_link = barcode_link
        super(Participante, self).save(*args, **kwargs)


# ----------------------------------------------------------------------
# ****************************** Comida ********************************
# ----------------------------------------------------------------------
class Comida(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    hora = models.DateTimeField(auto_now_add=True)
    tipo = models.IntegerField(choices=COMIDA_TIPOS)
