class Bike: 
    counter = 0  # Class attribute to track number of bikes created
    
    def __init__(self, description):
        self.description = description
        self.price = 100  # Default price
        self.discount = 0  # Default discount percentage
    
    def __repr__(self):
        return f"{self.__class__.__name__}(description={self.description!r}, price={self.price}, discount={self.discount})"

    @property
    def final_price(self):
        """Calculate final price after discount"""
        return self.price * (1 - self.discount / 100)
    
    @staticmethod
    def info():
        return "This is a Bike class representing a bike with pricing details."
    
    @classmethod
    def get_test_bike(cls):
        bike = cls(f"Test {cls.__name__}")
        cls.counter += 1
        return bike
    
    
class Unicycle(Bike):
    counter = 0


if __name__ == '__main__':
    bike = Bike('Mountain Bike')
    print(f"Base Price: ${bike.price}")
    print(f"Final Price (no discount): ${bike.final_price}")
    
    bike.discount = 15  # Apply a 15% discount
    print(f"Final Price (with 15% discount): ${bike.final_price}")
    
    bike_info = Bike.info()
    print(bike_info)    
    
    test_bike = Bike.get_test_bike()
    print(test_bike) 
    print("Total number of bikes: ", Bike.counter, "Total number of unicycles", Unicycle.counter)
    
    test_unicycle = Unicycle.get_test_bike()
    print(test_unicycle)
    print("Total number of bikes: ", Bike.counter, "Total number of unicycles", Unicycle.counter)