from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from tap_universiada.apps.comidas.models import Participante, Comida



def codigos(request):
    
    if request.POST:
        try:
            participante = Participante.objects.get(nombres=request.POST.get("nombre", ""))

            return render(request, 'codigos.html', {
            'participante': participante,
            'aprobado': True
            })
        except ObjectDoesNotExist:
            return render(request, 'codigos.html', {
                'mensaje': "No existe"
            })

    else:
        return render(request, 'codigos.html')
