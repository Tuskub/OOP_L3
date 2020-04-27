from abc import ABC, abstractmethod
from pizza.pizza import Pizza


class PizzaStore(ABC):

    @abstractmethod
    def _create_pizza(self, pizza_type: str) -> Pizza:
        pass

    def order_pizza(self, pizza_type: str) -> Pizza:
        pizza = self._create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
