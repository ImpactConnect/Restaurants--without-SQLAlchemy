class Customer():
    def _init__ (self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        
    def given_name(self):
        return self.given_name
    
    def family_name(self):
        return self.family_name
        
    def full_name(self, full_name):
        full_name = (f"{self.given_name}{self.family_name}")
        return full_name
    
    @classmethod
    def all(cls):
        return cls.quary.all
        