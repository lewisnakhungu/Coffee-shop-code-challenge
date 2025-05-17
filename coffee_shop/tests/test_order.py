
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_initialization():
    alice = Customer("Alice")
    espresso = Coffee("Espresso")
    order = Order(alice, espresso, 4.5)

    assert isinstance(order, Order)
    assert order.customer == alice
    assert order.coffee == espresso
    assert order.price == 4.5

def test_price_validation():
    alice = Customer("Alice")
    espresso = Coffee("Espresso")

    with pytest.raises(ValueError):
        Order(alice, espresso, -1)  # Invalid price

def test_order_repr():
    alice = Customer("Alice")
    espresso = Coffee("Espresso")
    order = Order(alice, espresso, 3.25)

    assert repr(order) == "<Order: customer=Alice, coffee=Espresso, price=3.25>"
