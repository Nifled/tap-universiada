from django.shortcuts import render


def index(request):
    hola = ""

    return render(request, 'index.html', {
      'hola': hola
    })
