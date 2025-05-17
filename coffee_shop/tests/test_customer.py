# tests/test_customer.py
# test_customer.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from customer import Customer


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
