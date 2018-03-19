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
    cena = [1, 2, 3, 4, 5]  # cena 6 a 11PM en UTC

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

        if participante.estatus:  # Si el estatus del jugador es en competencia

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

        else:

            # Si ya esta eliminado y ultima comida == False
            if not participante.estatus and not participante.ultima_comida:
                return render(request, 'codigos.html', {
                    'participante': participante,
                    'aprobado': False
                })

            # Check what day person was eliminated
            elimination_datetime = participante.datetime_eliminacion
            elimination_food_range = cual_rango_comida(elimination_datetime)  # rango de comida cuando fue eliminado

            # Pide su comida el mismo dia que fue eliminado
            if elimination_datetime.month == ahora.month and elimination_datetime.day == ahora.day:

                # Si quiere pedir comida en el rango de comida justo despues de su eliminacion
                if current_hour_range == elimination_food_range + 1:
                    # Set ultima comida falso
                    participante.ultima_comida = False
                    participante.save()

                    # Darle su ultima comida al hdp
                    Comida.objects.create(participante=participante, tipo=current_hour_range)

                    return render(request, 'codigos.html', {
                        'participante': participante,
                        'aprobado': True
                    })

                else:  # E.G. Fue eliminado en el desayuno y quiere pedir la cena del mismo dia, etc
                    return render(request, 'codigos.html', {
                        'participante': participante,
                        'aprobado': False
                    })

            # Si pide comer al dia despues de su eliminacion (No tiene validado si el siguiente
            # dia es el siguiente mes EG: March 31 - April 1)
            elif elimination_datetime.month == ahora.month and ahora.day == elimination_datetime.day + 1:
                # check if elimination hour range was dinner and ahora hour range is desayuno
                # elimination_food_range - rango cuando fue eliminado
                # current_hour_range  - rango de ahorita mismo

                # Si era cena ayer cuando lo eliminaron y ahorita es desayuno
                if elimination_food_range == 3 and current_hour_range == 1:
                    # Set ultima comida falso
                    participante.ultima_comida = False
                    participante.save()

                    # Darle su ultima comida al hdp
                    Comida.objects.create(participante=participante, tipo=current_hour_range)

                    return render(request, 'codigos.html', {
                        'participante': participante,
                        'aprobado': True
                    })

                else:  # El vato fue eliminado ayer en la cena y quiere comida o cena hoy
                    return render(request, 'codigos.html', {
                        'participante': participante,
                        'aprobado': False
                    })

            else:  # El vato fue eliminado y quiere pedir comida otro dia (2,3,4 dias despues, etc)
                return render(request, 'codigos.html', {
                    'participante': participante,
                    'aprobado': False
                })

    else:
        return render(request, 'codigos.html')
