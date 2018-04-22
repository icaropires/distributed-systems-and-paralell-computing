from functools import reduce
from django.core.management.base import BaseCommand, CommandError
from django.core.validators import ValidationError
from api.models import Matrix


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        while True:
            print('\n--------------------------------')
            print('Insira a opção desejada. Insira EXIT para sair')
            print('1. Registrar matriz')
            selection = input()

            if selection == 'EXIT':
                options = {
                    '1': self.register_matrix,
                }

                selected_option = options[selection]
                selected_option()
            else:
                break

    @staticmethod
    def register_matrix():
        name = input('Insira o nome para a matriz:')

        print('\nInsira a matrix linha por linha')
        print('Separe os elementos por espaço.'
              ' Use uma linha em branco para finalizar a inserção')

        matrix = Command.get_matrix()
        matrix = Command.matrix_to_string(matrix)

        try:
            matrix = Matrix.objects.create(name=name, matrix=matrix)
            print('Matriz registrada com sucesso!')
        except ValidationError:
            CommandError('Não foi possível registrar a matriz')

    @staticmethod
    def matrix_to_string(matrix):
        matrix = [str(row) for row in matrix]
        matrix = reduce(lambda x, y: x + y, matrix)

        return matrix

    @staticmethod
    def get_matrix():
        matrix = []
        while True:
            row = input()
            if row:
                elements = [int(element) for element in row.split()]
                matrix += [elements]
            else:
                break

        return matrix