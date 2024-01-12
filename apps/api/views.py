from django.shortcuts import render
from apps.app.models import Post, Comment
from .serializers import *
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required


class PostViewSet(viewsets.ModelViewSet):
    '''ViewSet para POSTS - APIRoot'''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete'] 

class CommentViewSet(viewsets.ModelViewSet):
    '''ViewSet para COMMENTS - APIRoot'''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete'] 
