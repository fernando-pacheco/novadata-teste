from rest_framework import serializers
from apps.app.models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    '''Serializer para o Post - APIRoot'''
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    '''Serializer para o Comment - APIRoot'''
    class Meta:
        model = Comment
        fields = '__all__'

