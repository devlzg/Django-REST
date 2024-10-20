from django.test import TestCase
from escola.models import Estudante, Curso

class FixturesTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def test_carregamento_da_fixtures(self):
        estudante = Estudante.objects.get(cpf='99224187463')
        curso = Curso.objects.get(pk=1)
        self.assertEqual(estudante.celular, '63 99532-4014')
        self.assertEqual(curso.codigo, 'POO')