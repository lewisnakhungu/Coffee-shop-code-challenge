class Coffee:
    def __init__(self, name):
        self.name =  name
        self._orders = []

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name (self, value):
        #set name attribute and validates lengtth
        if isinstance(value, str) and len(value)  >= 3:
             self._name = value
        else: raise ValueError("Name must be atleast 3 characters.")

    def orders(self):
        return self._orders
    
    def add_order(self, order):

        self._orders.append(order)
    
    def customers(self):
        #returns list of customers who have ordered this coffee
        # uses a set comprehension to avoid duplicates
        return list(set(order.customer for order in self._orders))
    
    def num_orders(self):
       # return total numbers this coffe has been ordered 
       return len(self._orders)
    
    def average_price(self):

        if self._orders:
            total_price = sum(order.price for order in self._orders)
            return total_price / len(self._orders)
        else:
            return 0.0 #return if no orders yet
            

    def __repr__ (self):
        return  f"<Coffee name = '{self.name}'>"
    