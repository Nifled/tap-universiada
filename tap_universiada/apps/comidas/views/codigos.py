from django.shortcuts import render

from tap_universiada.apps.comidas.models import Participante, Comida



def codigos(request):
    
    if request.POST:
        participante = Participante.objects.get(nombres=request.POST.get("nombre", ""))
        print()
  
        return render(request, 'codigos.html', {
        'participante': participante
        })
    else:
        return render(request, 'codigos.html')
