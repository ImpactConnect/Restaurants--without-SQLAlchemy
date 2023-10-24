from Review import review

class Restaurant:
    restaurants = []

    def __init__(self, name):
        self.name = name
        Restaurant.restaurants.append(self)

    def name(self):
        return self.name

    def reviews(self):
        restaurant_reviews = []
        for review in review.all():
            if review.restaurant() == self:
                restaurant_reviews.append(review)
        return restaurant_reviews

    def customers(self):
        reviewers = []
        for review in self.reviews():
            reviewers.append(review.customer())
        return list(set(reviewers))

    def average_star_rating(self):
        total_ratings = 0
        num_ratings = len(self.reviews())
        if num_ratings == 0:
            return 0
        for review in self.reviews():
            total_ratings += review.rating()
        return total_ratings / num_ratings

    
    