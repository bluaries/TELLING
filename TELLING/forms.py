from django import forms
from .models import Story, Chapter
from tinymce.widgets import TinyMCE

class StoryForm(forms.ModelForm):
    class Meta:
        model= Story
        fields= ("title", "categories", "thumbnail",)
    

class ChapterForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(mce_attrs={'width': 800}))
    class Meta:
        model= Chapter
        fields= ("title_chapter", "content",)