# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("HI!!, You're at the TELLING index.")

from django.shortcuts import render

def index(request):
    return render(request, 'base.html', {})