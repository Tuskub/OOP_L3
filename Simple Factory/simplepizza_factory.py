from pizza.pizza import Pizza
from pizza.cheese_pizza import CheesePizza
from pizza.veggie_pizza import VeggiePizza
from pizza.pepperoni_pizza import PepperoniPizza


class SimplePizzaFactory:

    def create_pizza(self, pizza_type: str) -> Pizza:

        switcher = {
            'cheese': CheesePizza(),
            'pepperoni': PepperoniPizza(),
            'veggie': VeggiePizza()
        }

        return switcher.get(pizza_type, Pizza())
