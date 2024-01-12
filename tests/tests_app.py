from rest_framework.test import APITestCase
from apps.app.models import Post, Comment
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User

class AppTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(author=self.user, title='Test Post', content='Test content')
        self.comment = Comment.objects.create(author=self.user, content='Test comment', post=self.post)