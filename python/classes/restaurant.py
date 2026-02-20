class Restaurant:
    """A simple attempt to model a resturant."""
    
    def __init__(self, resturantName, cuisineType):
        """Initialize resturant name and cuisine type attributes."""
        self.name = resturantName;
        self.cuisineType = cuisineType;
    
    def describeRestaurant(self):
        """Simulate Describe the resturant."""
        print(f"{self.name} serves {self.cuisineType} cuisine.");

    def openRestaurant(self):
        """Simulate opening the restaurant."""
        print(f"{self.name} is now open!");

myRestaurant = Restaurant('Pizza Hut', 'Italian');
myRestaurant.describeRestaurant();
myRestaurant.openRestaurant();

yourRestaurant = Restaurant('Chancellors', 'American');
yourRestaurant.describeRestaurant();
yourRestaurant.openRestaurant();

theirRestaurant = Restaurant('Sushi Boss', 'Japanese');
theirRestaurant.describeRestaurant();
theirRestaurant.openRestaurant();

