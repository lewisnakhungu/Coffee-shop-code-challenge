import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))



import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_initialization():
    latte = Coffee("Latte")
    assert isinstance(latte, Coffee)
    assert latte.name == "Latte"
    assert latte.orders() == []

def test_add_order_and_orders():
    coffee = Coffee("Espresso")
    customer = Customer("Alice")
    order = Order(customer, coffee, 3.0)

    coffee.add_order(order)
    assert order in coffee.orders()

def test_customers_returns_unique_customers():
    coffee = Coffee("Cappuccino")
    alice = Customer("Alice")
    bob = Customer("Bob")

    order1 = Order(alice, coffee, 3.0)
    order2 = Order(bob, coffee, 3.5)
    order3 = Order(alice, coffee, 4.0)

    coffee.add_order(order1)
    coffee.add_order(order2)
    coffee.add_order(order3)

    customers = coffee.customers()
    assert len(customers) == 2
    assert alice in customers and bob in customers
