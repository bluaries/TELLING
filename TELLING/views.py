from django.shortcuts import render
from .models import Story
from .forms import StoryForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_story'

    def get_queryset(self):
        return Story.objects.filter(date_posted__lte=timezone.now()).order_by('-date_posted')

def story_detail(request, pk):
    story = Story.objects.get(pk=pk)
    return render(request, "story_detail.html", {"story": story})

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

def create_chat(request):
    return render(request, 'create_chat.html')