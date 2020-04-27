from pizza.pizza import Pizza
from pizza.orenburg.orenburg_style_pizza import OrenburgStyleCheesePizza, OrenburgStylePepperoniPizza,\
    OrenburgStyleSolIletskPizza, OrenburgStyleVeggiePizza
from factories.pizza_store import PizzaStore


class NYStylePizzaStore(PizzaStore):

    def _create_pizza(self, pizza_type: str) -> Pizza:

        switcher = {
            'cheese': OrenburgStyleCheesePizza(),
            'pepperoni': OrenburgStylePepperoniPizza(),
            'salty': OrenburgStyleSolIletskPizza(),
            'veggie': OrenburgStyleVeggiePizza()
        }

        return switcher.get(pizza_type, Pizza())
