from pizza.pizza import Pizza
from pizza.chicago.chicago_style_pizza import ChicagoStyleCheesePizza,\
    ChicagoStylePepperoniPizza, ChicagoStyleVeggiePizza
from factories.pizza_store import PizzaStore


class ChicagoStylePizzaStore(PizzaStore):

    def _create_pizza(self, pizza_type: str) -> Pizza:

        switcher = {
            'cheese': ChicagoStyleCheesePizza(),
            'pepperoni': ChicagoStylePepperoniPizza(),
            'veggie': ChicagoStyleVeggiePizza()
        }

        return switcher.get(pizza_type, Pizza())
