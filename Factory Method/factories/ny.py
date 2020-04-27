from pizza.pizza import Pizza
from pizza.ny.cheesepizza import NYStyleCheesePizza
from pizza.ny.pepperoni import NYStylePepperoniPizza
from pizza.ny.vegiepizza import NYStyleVeggiePizza
from factories.pizza_store import PizzaStore


class NYStylePizzaStore(PizzaStore):

    def _create_pizza(self, pizza_type: str) -> Pizza:

        switcher = {
            'cheese': NYStyleCheesePizza(),
            'pepperoni': NYStylePepperoniPizza(),
            'veggie': NYStyleVeggiePizza()
        }

        return switcher.get(pizza_type, Pizza())
