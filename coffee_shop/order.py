class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        from customer import Customer
        if  isinstance(value, Customer):
            self._customer = value
        else:
            raise ValueError("customer must be an instance of Customer")
        
    @property
    def coffee(self):
        #getter for coffee attribute
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        #setter for the  coffee attribute with validation
        from coffee import Coffee
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise ValueError("coffee must be an instance of coffee")
        
    @property
    def price (self):
        return self._price
    

    @price.setter
    def price (self, value):
        #setter for price with validation (set price 1.0 and 10.0)
        if isinstance(value, float) and 1.0 <= value <= 10.0:
            self._price = value
        else:
            raise ValueError("price must be float between 1.0 and 10.0")
        

    def __repr__(self):
      return f"<Order: customer={self.customer.name}, coffee={self.coffee.name}, price={self.price}>"

        
    
        
