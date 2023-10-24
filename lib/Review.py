class Review():
    reviews = []

    def __init__ (self, customer, resturant, rating):
        self.customer = customer
        self.resturant = resturant
        self.rating = rating
        Review.reviews.append(self)
        
    def rating(self):
        return self.rating
    
    @classmethod
    def all(cls):
        return cls.reviews
    
    def customer(self,):
        return self.customer
    
    def restaurant(self):
        return self.restaurant