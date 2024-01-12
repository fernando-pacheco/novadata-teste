from django import forms
from .models import Post, Comment

class PostForms(forms.ModelForm):
    '''Form para o Post'''
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'cols': 40}),
        }


class CommentForms(forms.ModelForm):
    '''Form para o Comment'''
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'cols': 40}),
        }
        
class EditCommentForms(forms.ModelForm):
    '''Form para o Comment'''
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }