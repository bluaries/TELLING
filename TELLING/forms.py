from django import forms
from .models import Story
from tinymce.widgets import TinyMCE

class StoryForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(mce_attrs={'width': 800}))
    class Meta:
        model= Story
        fields= ("title","content", "author", "categories", "thumbnail",)
