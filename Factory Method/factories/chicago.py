from pizza.pizza import Pizza
from pizza.chicago.cheesepizza import ChicagoStyleCheesePizza
from pizza.chicago.pepperoni import ChicagoStylePepperoniPizza
from pizza.chicago.vegiepizza import ChicagoStyleVeggiePizza
from factories.pizza_store import PizzaStore


class ChicagoStylePizzaStore(PizzaStore):

    def _create_pizza(self, pizza_type: str) -> Pizza:

        switcher = {
            'cheese': ChicagoStyleCheesePizza(),
            'pepperoni': ChicagoStylePepperoniPizza(),
            'veggie': ChicagoStyleVeggiePizza()
        }

        return switcher.get(pizza_type, Pizza())
