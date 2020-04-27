from pizza.pizza import Pizza
from pizza.orenburg.cheesepizza import OrenburgStyleCheesePizza
from pizza.orenburg.pepperoni import OrenburgStylePepperoniPizza
from pizza.orenburg.salty import OrenburgStyleSolIletskPizza
from pizza.orenburg.vegiepizza import OrenburgStyleVeggiePizza
from factories.pizza_store import PizzaStore


class OrenburgStylePizzaStore(PizzaStore):

    def _create_pizza(self, pizza_type: str) -> Pizza:

        switcher = {
            'cheese': OrenburgStyleCheesePizza(),
            'pepperoni': OrenburgStylePepperoniPizza(),
            'salty': OrenburgStyleSolIletskPizza(),
            'veggie': OrenburgStyleVeggiePizza()
        }

        return switcher.get(pizza_type, Pizza())
