from django.shortcuts import render


def codigos(request):
    hola = "Hola mundo"

    return render(request, 'codigos.html', {
      'hola': hola
    })
