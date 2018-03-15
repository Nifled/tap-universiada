from django.contrib import admin
from django.shortcuts import render
from django.core import serializers

from .models import Disciplina, Equipo, Participante, Comida


def desactivar(modeladmin, request, queryset):
  queryset.update(estatus=False)
  queryset.update(ultima_comida=True)
  desactivar.short_description = "Marca los participantes eliminados"


def activar(modeladmin, request, queryset):
  queryset.update(estatus=True)

  for x in queryset:
    if x.ultima_comida == True:
      x.ultima_comida = False
      x.save()

    activar.short_description = "Activar participantes"


def imprimir(modeladmin, request, queryset):

    disciplinas = Disciplina.objects.all()

  
    return render(request, 'admin/canvas.html', {
        'queryset': serializers.serialize('json', queryset),
        'disciplinas': serializers.serialize('json', disciplinas)
    })


class ParticipanteAdmin(admin.ModelAdmin):
  list_display = ('nombres', 'apellido_p','apellido_m', 'estatus', 'institucion', 'tipo', 'disciplina')
  search_fields = ('nombres', 'apellido_p','apellido_m', 'institucion', 'tipo', 'disciplina__nombre')
  actions = [ desactivar, activar, imprimir ]

  

admin.site.register(Disciplina)
admin.site.register(Equipo)
admin.site.register(Participante, ParticipanteAdmin)
admin.site.register(Comida)

