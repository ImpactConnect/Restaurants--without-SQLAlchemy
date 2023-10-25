```markdown
# Yelp-style Domain Python Assignment

This Python assignment focuses on building a Yelp-style domain with three key models: `Restaurant`, `Customer`, and `Review`. The objective is to implement methods and relationships between these classes.

## Classes and Relationships

### Customer
- The `Customer` class represents a customer with a given name and family name.
- A customer can be initialized with a given name and family name.
- The `Customer` class provides methods to get and set the given name and family name.
- You can retrieve the full name of the customer in Western style.
- You can access a list of all customer instances.
- Find a customer by their full name.
- Find all customers with a given name.
- Retrieve the list of restaurants a customer has reviewed.
- Add a new review for a restaurant.

### Review
- The `Review` class represents a review with a customer, restaurant, and a rating.
- Reviews can be initialized with a customer, restaurant, and a rating.
- Get the rating for a review.
- Access a list of all review instances.
- Retrieve the customer and restaurant associated with a review.

### Restaurant
- The `Restaurant` class represents a restaurant with a name.
- Restaurants can be initialized with a name.
- Get the name of a restaurant.
- Access a list of reviews for a restaurant.
- Retrieve a list of customers who have reviewed a restaurant.
- Calculate the average star rating for a restaurant.

## Usage

1. Import the `Customer`, `Review`, and `Restaurant` classes in your Python program.
2. Create instances of customers, reviews, and restaurants.
3. Use the provided methods to manage and access customer and restaurant data.

## Example Usage

# Create customer, review, and restaurant instances
customer1 = Customer("John", "Doe")
restaurant1 = Restaurant("Delicious Diner")
review1 = Review(customer1, restaurant1, 4)

# Access customer and restaurant data
customer_full_name = customer1.full_name()
restaurant_name = restaurant1.name()
average_rating = restaurant1.average_star_rating()

# Add a new review for a restaurant
customer1.add_review(restaurant1, 5)
```

## Contributing

Contributions, bug reports, and suggestions are welcome. Feel free to open issues or pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

