from django.shortcuts import render
from .models import Story
from .forms import StoryForm

def index(request):
    queryset = Story.objects.filter()
    context = {
        'Stories': queryset
    }
    return render(request, 'index.html', context)

def create_story(request):
    form = StoryForm()
    return render(request, 'create_story.html', {'form': form})