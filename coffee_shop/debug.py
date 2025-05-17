from customer import Customer
from coffee import Coffee
from order import Order

alice = Customer("Alice")
bob = Customer("Bob")
latte = Coffee("Latte")
espresso = Coffee("Espresso")

alice.create_order(latte, 3.5)
alice.create_order(espresso, 4.5)
bob.create_order(latte, 4.0)

print(latte.customers())  # [Alice, Bob]
print(alice.coffees())    # [Latte, Espresso]
print(Coffee.average_price(latte))  # 3.75
print(Customer.most_aficionado(latte))  # Bob
