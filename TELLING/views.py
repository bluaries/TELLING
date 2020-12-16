from django.shortcuts import render
from .models import Story, Chapter, Category
from .forms import StoryForm, ChapterForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def index(request):
    search_stories = request.GET.get('search')
    if search_stories:
        stories = Story.objects.filter(Q(categories__category_name__icontains=search_stories) | Q(title__icontains=search_stories))
    else:
        stories = Story.objects.filter(date_posted__lte=timezone.now()).order_by('-date_posted')
    return render(request, 'index.html', {'stories': stories})

@login_required
def show_user_story(request):
    user_stories = Story.objects.filter(author=request.user)
    return render(request, 'user_story.html', {'user_stories': user_stories})

def story_detail(request, pk):
    story = Story.objects.get(pk=pk)
    return render(request, "story_detail.html", {"story": story})

def chapter_detail(request, pk):
    chapter = Chapter.objects.get(pk=pk)
    return render(request, "chapter.html", {"chapter": chapter})

def created_updated(model, request):
        obj = model.objects.latest('pk')
        if obj.author is None:
            obj.author = request.user
            obj.save()

@login_required
def create_story(request):
    if request.method == "POST":
        story_form = StoryForm(request.POST, request.FILES)
        if story_form.is_valid():
            story_form.save()
            img_obj = story_form.instance
            created_updated(Story, request)
            return HttpResponseRedirect(reverse('TELLING:homepage'))
    else:
        story_form = StoryForm()
    return render(request, 'create_story.html', {'story_form': story_form})

@login_required
def edit_story(request, pk):
    this_story = Story.objects.get(pk=pk)
    if request.method == "POST":
        update_story_form = StoryForm(request.POST, instance=this_story)
        if update_story_form.is_valid():
            this_story.save()
            return HttpResponseRedirect(reverse('TELLING:homepage'))
    else:
        update_story_form = StoryForm(instance=this_story)
        return render(request, 'edit_story.html', {'update_story_form': update_story_form, 'story': this_story})

@login_required
def create_new_chapter(request, pk):
    add_to_story = Story.objects.get(pk=pk)
    if request.method == "POST":
        chapter_form = ChapterForm(request.POST, user=request.user)
        if chapter_form.is_valid():
            chapter_form.save()
            return HttpResponseRedirect(reverse('TELLING:homepage'))
    else:
        chapter_form = ChapterForm(user=request.user)
    return render(request, 'create_chapter.html', {'chapter_form': chapter_form, 'story': add_to_story})

@login_required
def edit_chapter(request, pk):
    this_chap = Chapter.objects.get(pk=pk)
    if request.method == "POST":
        update_chapter_form = ChapterForm(request.POST, instance=this_chap)
        if update_chapter_form.is_valid():
            this_chap.save()
            return HttpResponseRedirect(reverse('TELLING:homepage'))
    else:
        update_chapter_form = ChapterForm(instance=this_chap)
    return render(request, 'edit_chapter.html', {'update_chapter_form': update_chapter_form, 'chapter': this_chap})


