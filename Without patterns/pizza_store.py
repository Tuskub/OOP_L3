from pizza.pizza import Pizza
from pizza.chicago.cheesepizza import ChicagoStyleCheesePizza
from pizza.chicago.pepperoni import ChicagoStylePepperoniPizza
from pizza.chicago.veggiepizza import ChicagoStyleVeggiePizza
from pizza.ny.cheesepizza import NYStyleCheesePizza
from pizza.ny.pepperoni import NYStylePepperoniPizza
from pizza.ny.veggiepizza import NYStyleVeggiePizza
from pizza.orenburg.cheesepizza import OrenburgStyleCheesePizza
from pizza.orenburg.pepperoni import OrenburgStylePepperoniPizza
from pizza.orenburg.salty import OrenburgStyleSolIletskPizza
from pizza.orenburg.veggiepizza import OrenburgStyleVeggiePizza


class PizzaStore:

    def order_pizza(self, branch: str, pizza_type: str) -> Pizza:
        switcher = {
            'chicago': {
              'cheese': ChicagoStyleCheesePizza,
              'pepperoni': ChicagoStylePepperoniPizza,
              'veggie': ChicagoStyleVeggiePizza
            },
            'new york': {
                'cheese': NYStyleCheesePizza,
                'pepperoni': NYStylePepperoniPizza,
                'veggie': NYStyleVeggiePizza
            },
            'orenburg': {
                'cheese': OrenburgStyleCheesePizza,
                'pepperoni': OrenburgStylePepperoniPizza,
                'salty': OrenburgStyleSolIletskPizza,
                'veggie': OrenburgStyleVeggiePizza
            }
        }

        pizza = switcher.get(branch).get(pizza_type, Pizza())()

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
