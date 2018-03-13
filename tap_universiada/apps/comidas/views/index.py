from django.shortcuts import render


def index(request):
    hola = "Hola mundo"

    return render(request, 'index.html', {
      'hola': hola
    })
