from factories.chicago import ChicagoStylePizzaStore
from factories.ny import NYStylePizzaStore
from factories.orenburg import OrenburgStylePizzaStore


test = NYStylePizzaStore()
ny_pizza = test.order_pizza('pepperoni')
print(ny_pizza.description)


test2 = ChicagoStylePizzaStore()
chicago_pizza = test2.order_pizza('pepperoni')
print(chicago_pizza.description)


test3 = OrenburgStylePizzaStore()
orenburg_pizza = test3.order_pizza('salty')
print(orenburg_pizza.description)
