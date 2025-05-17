class Customer:
    
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property #getter
    def name(self):
        return self._name 
    
    @name.setter
    def name (self, value):

        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")
        
    def orders(self):
        #returns list of orders for this customer
        return self._orders
    
    def add_order(self, order):
        #appends single prder to the customer order list
        self._orders.append(order)

    def coffees(self):
        # return unique list of customer order list
        return list(set(order.coffee for order in self._orders))
    
    def create_order(self, coffee, price):
        #creates new order for this customer and a specific coffee.. imports orders.py avoids circular dependency

        from order import Order
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        coffee.add_order(new_order)
        return new_order
    
    @classmethod
    def most_aficionado(cls, coffee):
        #finds customer who spent most money on given coffee

        top_customer = None
        top_spent = 0 

        for order in coffee.orders():
            customer = order.customer

            total = sum(o.price for o in customer.orders() if o.coffee == coffee)

            #updates top customer if another spents more
            if total > top_spent:
                top_customer = customer
                top_spent = total

        return top_customer 
    
    def __repr__(self):
        return f"<Customer name = '{self.name}'>"



