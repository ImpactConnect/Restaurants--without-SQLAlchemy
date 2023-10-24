from Customer import Customer

class Review():
    def __init__ (self, customer, resturant, rating):
        self.customer = customer
        self.resturant = resturant
        self.rating = rating
        
    def rating(self):
        return self.rating
    
    @classmethod
    def all(cls):
        return cls.all
    
    def customer(self,):
        return self.customer
    
    def restaurant(self):
        return self.restaurant