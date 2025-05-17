# Coffee-shop-code-challenge
# Coffee Shop Domain Modeling Project

This project models a coffee shop system using Object-Oriented Programming (OOP) in Python. It includes three main classes:

* `Customer`
* `Coffee`
* `Order`

These classes interact to simulate real-world relationships, such as customers ordering coffee, and tracking spending habits.

## Features

* Customers can place multiple orders.
* Orders are linked to specific coffee types and customers.
* Coffees can track their orders and customers.
* A method to find the customer who spent the most on a specific coffee (`most_aficionado`).

## Project Structure

```
coffee_shop/
├── coffee.py
├── customer.py
├── order.py
├── debug.py
├── tests/
│   ├── test_customer.py
│   ├── test_coffee.py
│   └── test_order.py
├── Pipfile
├── Pipfile.lock
└── README.md
```

## Running the Project

To run the project and tests:

### 1. Set Up Environment

```bash
pipenv install --dev
pipenv shell
```

### 2. Run the Debug Script

```bash
python coffee_shop/debug.py
```

### 3. Run Tests

```bash
pytest
```

## Key Classes

### `Customer`

* `name` with validation (1-15 chars).
* `create_order(coffee, price)` links to both customer and coffee.
* Tracks its own list of orders.
* Class method `most_aficionado(coffee)` returns the top customer for that coffee.

### `Coffee`

* Initialized with `name`.
* Tracks a list of orders.
* Returns a list of customers who ordered it.

### `Order`

* Created with a `Customer`, `Coffee`, and `price`.
* Linked bidirectionally using `create_order()` method.

## Sample Usage

```python
alice = Customer("Alice")
latte = Coffee("Latte")
alice.create_order(latte, 3.5)
```

## Testing Highlights

* Test for valid/invalid customer names.
* Test that orders are correctly linked.
* Test that the most aficionado logic works.

---
