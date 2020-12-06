from django import forms
from .models import Story, Chapter
from tinymce.widgets import TinyMCE

class StoryForm(forms.ModelForm):
    class Meta:
        model= Story
        fields= ("title", "categories", "thumbnail",)
        widgets= {
            'title':forms.TextInput(attrs={
            'class': 'form-control', 'style':'width:80%',
            'placeholder': 'Write your title here'})
        }
    

class ChapterForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(mce_attrs={'width': 800}))
    class Meta:
        model= Chapter
        fields= ("title_chapter", "content",)