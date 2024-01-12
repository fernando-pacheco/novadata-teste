from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from apps.app.models import Post, Comment

class PostAPITestCase(TestCase):
    def setUp(self):
        '''Função para realizar o setup das informações de teste'''
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()

    def test_read_post_list(self):
        '''Teste para leitura da lista de posts'''
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_post_detail(self):
        '''Teste para leitura de um post'''
        post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        response = self.client.get(f'/api/posts/{post.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        '''Teste para criação de um post'''
        new_post_data = {'title': 'New Test Post', 'content': 'New Test Content', 'author': self.user.id}
        response = self.client.post('/api/posts/', data=new_post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_post(self):
        '''Teste para atualização de um post'''
        post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        updated_title = 'Updated Test Post'
        data = {'title': updated_title}
        response = self.client.patch(f'/api/posts/{post.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post.refresh_from_db()
        self.assertEqual(post.title, updated_title)

    def test_delete_post(self):
        '''Teste para exclusão de um post'''
        post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        response = self.client.delete(f'/api/posts/{post.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
