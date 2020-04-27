from abc import ABC


class Pizza(ABC):
    description: str = 'Пицца'

    def prepare(self):
        print('Prepare')

    def bake(self):
        print('bake')

    def cut(self):
        print('cut')

    def box(self):
        print('box')
