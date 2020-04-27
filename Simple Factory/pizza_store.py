from dataclasses import dataclass
from simplepizza_factory import SimplePizzaFactory
from pizza.pizza import Pizza


@dataclass()
class PizzaStore:
    fabric: SimplePizzaFactory

    def order_pizza(self, pizza_type: str) -> Pizza:
        pizza = self.fabric.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
