from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from apps.app.models import Post, Comment

class CommentAPITestCase(TestCase):
    def setUp(self):
        '''Função para realizar o setup das informações de teste'''	
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        self.comment_data = {'post': self.post, 'content': 'Test Comment', 'author': self.user}
        self.comment = Comment.objects.create(**self.comment_data)
        self.client = APIClient()

    def test_read_comment_list(self):
        '''Teste para leitura da lista de comentários'''
        response = self.client.get('/api/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_comment_detail(self):
        '''Teste para leitura de um comentário'''
        response = self.client.get(f'/api/comments/{self.comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_comment(self):
        '''Teste para criação de um comentário'''
        new_comment_data = {'post': self.post.id, 'content': 'New Comment', 'author': self.user.id}
        response = self.client.post('/api/comments/', data=new_comment_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_comment(self):
        '''Teste para atualização de um comentário'''
        updated_content = 'Updated Test Comment'
        data = {'content': updated_content}
        response = self.client.patch(f'/api/comments/{self.comment.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, updated_content)


    def test_delete_comment(self):
        '''Teste para exclusão de um comentário'''
        response = self.client.delete(f'/api/comments/{self.comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
