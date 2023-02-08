from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html', {'heading': 'CALCULATOR (Adding Two Numbers)'})


def add(request):
    val1 = int(request.GET['first'])
    val2 = int(request.GET['second'])
    res = val1 + val2
    return render(request, 'result.html', {'result': res})
