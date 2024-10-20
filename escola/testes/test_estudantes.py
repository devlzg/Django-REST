from django.contrib.auth. models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class EstudantesTestCase(APITestCase):
    fixtures = ['prototipo_banco.py']
    def setUp(self):
        # self.usuario = User.objects.create_superuser(
        #     username='admin',
        #     password='admin')
        self.usuario = User.objects.get(username='luiz')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        # self.estudante_01 = Estudante.objects.create(
        #     nome = 'Teste estudante UM', 
        #     email = 'testeestudante1@gmail.com', 
        #     cpf = '68449331005',
        #     data_nascimento = '2024-10-20',
        #     celular = '61 91234-5678'              
        # )
        self.estudante_01 = Estudante.objects.get(pk=1)

        # self.estudante_02 = Estudante.objects.create(
        #     nome = 'Teste estudante DOIS', 
        #     email = 'testeestudante2@gmail.com', 
        #     cpf = '69110291040',
        #     data_nascimento = '2024-10-20',
        #     celular = '61 91234-5678'              
        # )
        self.estudante_02 = Estudante.objects.get(pk=2)
    
    def test_requisicao_get_para_listar_estudantes(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_requisicao_get_para_listar_um_estudante(self):
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(pk=1)
        dados_estudante_serializados = EstudanteSerializer(instance=dados_estudante).data
        self.assertEqual(response.data, dados_estudante_serializados)

    def test_requisicao_post_para_criar_um_estudante(self):
        dados = {
            'nome': 'teste',
            'email': 'teste@email.com',
            'cpf': '49180908004',
            'data_nascimento': '2024-07-28',
            'celular': '61 99999-9999',
        }
        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_requisicao_delete_um_estudante(self):
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_requisicao_put_para_criar_atualizar_estudante(self):
        dados = {
            'nome': 'testeput',
            'email': 'testeput@email.com',
            'cpf': '63924901082',
            'data_nascimento': '2024-04-29',
            'celular': '61 99999-8888',
        }
        response = self.client.put(self.url+'1/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)