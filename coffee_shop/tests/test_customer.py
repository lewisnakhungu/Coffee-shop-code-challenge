
# tests/test_customer.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from customer import Customer
from coffee import Coffee
from order import Order  # ✅ You need this to avoid NameError
import pytest

def test_customer_name_valid():
    c = Customer("John")
    assert c.name == "John"

def test_customer_name_invalid():
    with pytest.raises(ValueError):
        Customer("")

def test_customer_name_too_long():
    with pytest.raises(ValueError):
        Customer("x" * 16)

def test_most_aficionado():
    # Create customers
    alice = Customer("Alice")
    bob = Customer("Bob")
    clara = Customer("Clara")

    # Create coffee
    latte = Coffee("Latte")

    # Use the create_order method to ensure everything is wired correctly
    alice.create_order(latte, 3.5)
    alice.create_order(latte, 4.0)
    bob.create_order(latte, 3.5)
    clara.create_order(latte, 2.0)
    clara.create_order(latte, 2.5)

    # Now this should pass
    assert Customer.most_aficionado(latte) == alice
