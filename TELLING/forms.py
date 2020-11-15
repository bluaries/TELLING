from django import forms
from .models import Story

class StoryForm(forms.ModelForm):
    class Meta:
        model= Story
        fields= ("title","content", "author", "categories", "thumbnail",)
