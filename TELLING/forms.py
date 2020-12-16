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
    content = forms.CharField(widget=TinyMCE(mce_attrs={'width': 800, 'height':800}))
    class Meta:
        model= Chapter
        fields= ("story", "title_chapter", "content",)

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            story = self.fields['story']
            story.queryset = story.queryset.filter(author=user)
