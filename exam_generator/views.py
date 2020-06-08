# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,
                  'home.html',
                  {'test': 'successful string interpolation test.'})
