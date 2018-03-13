from django.db import models

from .choices import *


# ----------------------------------------------------------------------
# **************************** Disciplina ******************************
# ----------------------------------------------------------------------
class Disciplina(models.Model):
    nombre = models.CharField(max_length=85)

    def __str__(self):
        return self.nombre


# ----------------------------------------------------------------------
# ****************************** Equipo ********************************
# ----------------------------------------------------------------------
class Equipo(models.Model):
    pass


# ----------------------------------------------------------------------
# *************************** Participante *****************************
# ----------------------------------------------------------------------
class Participante(models.Model):
    nombres = models.CharField(max_length=85)
    apellido_p = models.CharField(max_length=45, verbose_name='Apellido Paterno')
    apellido_m = models.CharField(max_length=45, verbose_name='Apellido Materno')
    estatus = models.BooleanField(default=True)  # True = en competencia, False = eliminado
    institucion = models.CharField(max_length=85)
    tipo = models.IntegerField(choices=PARTICIPANTE_TIPOS)  # Choices en ./choices.py

    # `estatos` == False (eliminado) y `ultima_comida` == True, ya no puede comer nunca.
    ultima_comida = models.BooleanField(default=False)

    # Foreign Keys
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)  # TODO : change on_delete
    equipo = models.ForeignKey(Equipo, blank=True, null=True, on_delete=models.SET_NULL)  # propiedad opcional

    def __str__(self):
        return '{} - {}, Estatus: {}'\
            .format(self.apellido_p, self.disciplina.nombre, self.estatus)


# ----------------------------------------------------------------------
# ****************************** Comida ********************************
# ----------------------------------------------------------------------
class Comida(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    hora = models.DateTimeField(auto_now_add=True)
    tipo = models.IntegerField(choices=COMIDA_TIPOS)