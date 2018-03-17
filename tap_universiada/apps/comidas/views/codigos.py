from datetime import datetime
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from tap_universiada.apps.comidas.models import Participante, Comida


def cual_rango_comida(datetime_obj):
    """
    Recibe una hora, devuelve
    1 si es en desayuno,
    2 si es comida,
    3 si es cena,
    0 si no esta en ningun rango
    """
    desayuno = [14, 15, 16]  # desayuno 7 a 10AM en UTC
    comida = [20, 21, 22]  # comida 1 a 4PM en UTC
    cena = [3, 4, 5]  # cena 8 a 11PM en UTC

    hora_actual = datetime_obj.hour
    print (hora_actual)
    if hora_actual in desayuno:
        print("desayuno")
        return 1

    elif hora_actual in comida:
        print("Es comida")
        return 2

    elif hora_actual in cena:
        print("Es cena")
        return 3

    else:
        print("no esta en el rango")
    return 0


def codigos(request):

    if request.POST:
        try:
            participante = Participante.objects.get(barcode=request.POST.get("nombre", ""))

        except ObjectDoesNotExist:
            return render(request, 'codigos.html', {
                'mensaje': "No existe"
            })

        ahora = datetime.now()  # Obtiene fecha y hora actual

        # Get current time & range
        current_hour_range = cual_rango_comida(ahora)  # 1=desayuno, 2=comida, 3=cena

        if current_hour_range == 0:  # No estamos al rango para comer ahorita!
            return render(request, 'codigos.html', {
                'participante': participante,
                'aprobado': False
            })

        # Check if user has already eaten in time range
        # Filter database for Comida object

        # Get most recent Comida obj
        # last_comida = Comida.objects.filter(participante=participante).order_by('-hora')[0]
        last_comida_queryset = Comida.objects.filter(participante=participante).order_by('-hora')

        if not last_comida_queryset.exists():  # If no comida object exists

            # Create Comida object
            Comida.objects.create(participante=participante, tipo=current_hour_range)
            return render(request, 'codigos.html', {
                'participante': participante,
                'aprobado': True
            })

        else:  # If object exists, get last Comida obj
            last_comida = last_comida_queryset[0]

        # Checar si la ultima comida que comio el vato fue hoy
        if last_comida.hora.month == ahora.month and last_comida.hora.day == ahora.day:

            if cual_rango_comida(last_comida.hora) == current_hour_range:
                # Si esto es verdadero, el vato ya desayuno y quiere volver a desayunar el hdp
                return render(request, 'codigos.html', {
                    'participante': participante,
                    'aprobado': False
                })

            else:  # El vato no ha comido la comida de este rango todavia

                # Create Comida object
                Comida.objects.create(participante=participante, tipo=current_hour_range)
                return render(request, 'codigos.html', {
                    'participante': participante,
                    'aprobado': True
                })

        else:  # Si no es el mismo dia pues puede comer (por ahorita)

            # Create Comida object
            Comida.objects.create(participante=participante, tipo=current_hour_range)
            
            return render(request, 'codigos.html', {
                'participante': participante,
                'aprobado': True
            })

        # TODO : Falta hacer las validaciones para lo de la ultima comida

    else:
        return render(request, 'codigos.html')
