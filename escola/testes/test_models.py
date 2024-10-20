from django.test import TestCase
from escola.models import Estudante, Curso, Matricula

class ModelEstudanteTestCase(TestCase):
    # def teste_falha(self):
    #     self.fail('Teste falhou :(')
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo', 
            email = 'testedemodelo@gmail.com', 
            cpf = '68449331005',
            data_nascimento = '2024-10-20',
            celular = '61 91234-5678'
        )
    
    def test_verifica_atributos_de_estudante(self):
        """Teste que verifica os atributos do modelo de Estudante"""
        self.assertEqual(self.estudante.nome, 'Teste de Modelo')
        self.assertEqual(self.estudante.email, 'testedemodelo@gmail.com')
        self.assertEqual(self.estudante.cpf, '68449331005')
        self.assertEqual(self.estudante.data_nascimento, '2024-10-20')
        self.assertEqual(self.estudante.celular, '61 91234-5678')
        
class ModelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = 'TestModeloCurso', 
            descricao = 'teste do modelo Curso', 
            nivel = 'B',
        )
    
    def test_verifica_atributos_de_curso(self):
        """Teste que verifica os atributos do modelo de Curso"""
        self.assertEqual(self.curso.codigo, 'TestModeloCurso')
        self.assertEqual(self.curso.descricao, 'teste do modelo Curso')
        self.assertEqual(self.curso.nivel, 'B')

class ModelMatriculaTestCase(TestCase):
    def setUp(self):
        self.matricula = Matricula.objects.create(
            estudante = Estudante.objects.create(
                        nome = 'Teste de Modelo', 
                        email = 'testedemodelo@gmail.com', 
                        cpf = '68449331005',
                        data_nascimento = '2024-10-20',
                        celular = '61 91234-5678'
                        ), 
            curso = Curso.objects.create(
                        codigo = 'TestModeloCurso', 
                        descricao = 'teste do modelo Curso', 
                        nivel = 'B',
                        ), 
            periodo = 'M',
        )
    
    def test_verifica_atributos_de_curso(self):
        """Teste que verifica os atributos do modelo de Curso"""
        self.assertEqual(self.matricula.estudante.nome, 'Teste de Modelo')
        self.assertEqual(self.matricula.estudante.email, 'testedemodelo@gmail.com')
        self.assertEqual(self.matricula.estudante.cpf, '68449331005')
        self.assertEqual(self.matricula.estudante.data_nascimento, '2024-10-20')
        self.assertEqual(self.matricula.estudante.celular, '61 91234-5678')
        self.assertEqual(self.matricula.curso.codigo, 'TestModeloCurso')
        self.assertEqual(self.matricula.curso.descricao, 'teste do modelo Curso')
        self.assertEqual(self.matricula.curso.nivel, 'B')
        self.assertEqual(self.matricula.periodo, 'M')