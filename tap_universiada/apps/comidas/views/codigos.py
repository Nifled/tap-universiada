from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, date, time, timedelta
import calendar

from tap_universiada.apps.comidas.models import Participante, Comida

def comidaActual():
	ahora = datetime.now()  # Obtiene fecha y hora actual
  	
	horaactual = ahora.hour
    #desayno 7 a 10
    #comida 1 a 4
    #cena 8 a 11
	if horaactual == 7 or horaactual == 8 or horaactual == 9 or horaactual == 10:
		print ("desayuno")
		return 0

	elif horaactual == 13 or horaactual == 14 or horaactual == 15 or horaactual == 16:
  		print ("Es comida")
  		return 1

	elif horaactual == 20 or horaactual == 21 or horaactual == 22 or horaactual == 23:
 		print ("Es cena")
 		return 2

	else :
		print ("no esta en el rango")
	return 3




def codigos(request):
    print (comidaActual())
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
