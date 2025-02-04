from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Postagem

class PostagemViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.postagem = Postagem.objects.create(titulo='Teste', autor=self.user, artigo='Conteúdo de teste')

    def test_listar_postagens(self):
        response = self.client.get('/api/postagens/')
        self.assertEqual(response.status_code, 200)

    def test_criar_postagem(self):
        data = {'titulo': 'Nova Postagem', 'artigo': 'Conteúdo da nova postagem'}
        response = self.client.post('/api/postagens/', data)
        self.assertEqual(response.status_code, 201)