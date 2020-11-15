from django.shortcuts import render
from .models import Story
from .forms import StoryForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def index(request):
    queryset = Story.objects.filter()
    context = {
        'Stories': queryset
    }
    return render(request, 'index.html', context)



def create_story(request):
    if request.method == "POST":
        story_form = StoryForm(request.POST, request.FILES)
        if story_form.is_valid():
            story_form.save()
            img_obj = story_form.instance
            return HttpResponseRedirect(reverse('TELLING:homepage'))
    else:
        story_form = StoryForm()
    return render(request, 'create_story.html', {'story_form': story_form})