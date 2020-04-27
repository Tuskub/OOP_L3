from pizza_store import PizzaStore


test = PizzaStore()
ny_pizza = test.order_pizza('new york', 'pepperoni')
print(ny_pizza.description)


test2 = PizzaStore()
chicago_pizza = test2.order_pizza('chicago', 'pepperoni')
print(chicago_pizza.description)


test3 = PizzaStore()
orenburg_pizza = test3.order_pizza('orenburg', 'salty')
print(orenburg_pizza.description)
