from django.shortcuts import render
from tap_universiada.apps.comidas.models import Participante, Comida, Disciplina
from tap_universiada.apps.comidas.choices import PARTICIPANTE_TIPOS
from functools import reduce

def tablas(request):
    comidas = Comida.objects.all()

    comidas_por_tipo_participante = [
      [
        [],[],[]
      ],[
        [],[],[]
      ],[
        [],[],[]
      ],[
        [],[],[]
      ],[
        [],[],[]
      ],[
        [],[],[]
      ],[
        [],[],[]
      ],[
        [],[],[]
      ]
    ]

    for comida in comidas:
      comidas_por_tipo_participante[comida.participante.tipo - 1][comida.tipo - 1].append(comida)
  
  
    total_desayunos = reduce((lambda x, y: 
      x + len(y[0])
      if type(x) is not list
      else 
      len(x[0]) + len(y[0])
    ), comidas_por_tipo_participante)


    total_comidas = reduce((lambda x, y: 
      x + len(y[1])
      if type(x) is not list
      else 
      len(x[1]) + len(y[1])
    ), comidas_por_tipo_participante)

    total_cenas = reduce((lambda x, y: 
      x + len(y[2])
      if type(x) is not list
      else 
      len(x[2]) + len(y[2])
    ), comidas_por_tipo_participante)




    return render(request, 'tablas.html', {
      'comidas' : comidas_por_tipo_participante,
      'total_desayunos': total_desayunos,
      'total_comidas': total_comidas,
      'total_cenas': total_cenas,

      'total_deportista': reduce((lambda x, y: 
        x + len(y)
        if type(x) is not list
        else 
        len(x) + len(y)
      ), comidas_por_tipo_participante[0]),
      'total_entrenador': reduce((lambda x, y: 
        x + len(y)
        if type(x) is not list
        else 
        len(x) + len(y)
      ), comidas_por_tipo_participante[1]),

      'total_juez': reduce((lambda x, y: 
        x + len(y)
        if type(x) is not list
        else 
        len(x) + len(y)
      ), comidas_por_tipo_participante[2]),
      
      'total_delegado': reduce((lambda x, y: 
        x + len(y)
        if type(x) is not list
        else 
        len(x) + len(y)
      ), comidas_por_tipo_participante[3]),
      'total_coordinador': reduce((lambda x, y: 
        x + len(y)
        if type(x) is not list
        else 
        len(x) + len(y)
      ), comidas_por_tipo_participante[4]),
      'total_comisionado': reduce((lambda x, y: 
        x + len(y)
        if type(x) is not list
        else 
        len(x) + len(y)
      ), comidas_por_tipo_participante[5]),
      'total_medico': reduce((lambda x, y: 
        x + len(y)
        if type(x) is not list
        else 
        len(x) + len(y)
      ), comidas_por_tipo_participante[6]),
      'total_comite': reduce((lambda x, y: 
        x + len(y)
        if type(x) is not list
        else 
        len(x) + len(y)
      ), comidas_por_tipo_participante[7]),
      'total': total_desayunos + total_comidas + total_cenas


    })
