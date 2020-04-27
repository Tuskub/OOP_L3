from pizza_store import PizzaStore
from simplepizza_factory import SimplePizzaFactory


test = PizzaStore(SimplePizzaFactory())
pizza = test.order_pizza('gdfs')
print(pizza.description)
