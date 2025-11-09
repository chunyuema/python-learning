from enum import Enum


class Condition(Enum):
    NEW = 0
    GOOD = 1
    OKAY = 2
    BAD = 3


class MethodNotAllowed(Exception):
    pass


class Bike(object):
    def __init__(self, description, condition, sale_price, cost=0):
        self.description = description
        self.condition = condition
        self.sale_price = sale_price
        self.cost = cost
        self.sold = False

    # Destructor: Called when an object is about to be destroyed
    # Note: this does not release memory, Python's garbage collector handles that
    def __del__(self):
        print(f'Deleting bike: {self.description}')

    def update_sale_price(self, sale_price):
        if self.sold:
            raise MethodNotAllowed('Action not allowed. Bike has already been sold')
        self.sale_price = sale_price

    def sell(self):
        """
        Mark as sold and determine the profit received from selling the bike
        """
        self.sold = True
        profit = self.sale_price - self.cost
        return profit

    def service(self, spent, sale_price=None, condition=None):
        """
        Service the bike and update attributes
        """
        self.cost += spent
        if sale_price:
            self.update_sale_price(sale_price)
        if self.condition:
            self.condition = condition

    def __repr__(self):
        print('__repr__ called')
        # repr of string should be unambiguous
        return f"Bike({self.description!r}, {self.condition}, {self.sale_price}, {self.cost})"

    def __str__(self):
        print('__str__ called')
        return self.description


if __name__ == '__main__':
    bike = Bike('Univega Alpina, orange', Condition.OKAY, sale_price=500, cost=100)
    bike2 = Bike('Univega Alpina, orange', Condition.OKAY, sale_price=500, cost=100)
    
    print("====== Equality comparison: ======")
    print(bike == bike2)  # False, default is identity comparison)

    print("====== String representations: ======")
    print(bike)        # __str__ called
    print(str(bike))   # __str__ called
    print("\n")

    print("====== Official representations: ======")
    print([bike])      # __repr__ called
    print(repr(bike))  # __repr__ called
    print("\n")
    

    print("====== Deleting bike: ======")
    del bike           # __del__ called
    Bike('Raleigh Talus 2', Condition.BAD, sale_price=20)  # __init__ and __del__ called
    print("\n")
    