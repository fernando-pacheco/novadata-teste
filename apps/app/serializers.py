from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    '''Serializer para o Post'''
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    '''Serializer para o Comment'''
    class Meta:
        model = Comment
        fields = '__all__'

