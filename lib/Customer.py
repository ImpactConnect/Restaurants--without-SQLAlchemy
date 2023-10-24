from Review import review

class Customer():
    customers = []
    
    def _init__ (self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.customers.append(self)
        
    def given_name(self):
        return self.given_name
    
    def family_name(self):
        return self.family_name
        
    def full_name(self, full_name):
        full_name = (f"{self.given_name}{self.family_name}")
        return full_name
    
    @classmethod
    def all(cls):
        return cls.customers
        
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.customers:
            if customer.full_name() == name:
                return customer
            
    @classmethod
    def find_all_by_given_name(cls, given_name):
        matching_customers = []
        for customer in cls.customers:
            if customer.given_name == given_name:
                matching_customers.append(customer)
        return matching_customers
    
    def restaurants(self):
        reviewed_restaurants = []
        for review in review.all():
            if review.customer() == self:
                reviewed_restaurants.append(review.restaurant())
        return list(set(reviewed_restaurants))  
    
    def add_review(self, restaurant, rating):
        review(self, restaurant, rating)