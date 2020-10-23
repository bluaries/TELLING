from django.http import HttpResponse


def index(request):
    return HttpResponse("HI!!, You're at the TELLING index.")