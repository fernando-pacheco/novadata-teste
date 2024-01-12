from rest_framework.test import APITestCase
from apps.users.forms import CadastroForms, LoginForms
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User

class AppTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        