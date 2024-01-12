from django import forms
from .models import Post, Comment

class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'cols': 40}),
        }


class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content', 'post']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'cols': 40}),
        }
        
