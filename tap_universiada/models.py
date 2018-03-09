from django.db import models

class Disciplina(models.Model):
  nombre = models.CharField(max_length=30)