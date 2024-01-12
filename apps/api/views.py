from django.shortcuts import render
from apps.app.models import Post, Comment
from .serializers import *
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete'] 

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete'] 
