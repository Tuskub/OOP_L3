from abc import ABC


class Pizza(ABC):
    description: str = 'Пицца'

    def prepare(self):
        print(f'Prepare \"{self.description}\"')

    def bake(self):
        print(f'Baking \"{self.description}\"')

    def cut(self):
        print(f'Cutting \"{self.description}\"')

    def box(self):
        print(f'Putting \"{self.description}\" in box')
