from django.shortcuts import render
from .models import Story


def index(request):
    queryset = Story.objects.filter()
    context = {
        'Stories': queryset
    }
    return render(request, 'index.html', context)
