class Restaurant:
    """A simple attempt to model a resturant."""
    
    def __init__(self, resturantName, cuisineType, ):
        """Initialize resturant name and cuisine type attributes."""
        self.name = resturantName;
        self.cuisineType = cuisineType;
        self.numberServed = 0;
    
    def describeRestaurant(self):
        """Simulate Describe the resturant."""
        print(f"{self.name} serves {self.cuisineType} cuisine.");

    def openRestaurant(self):
        """Simulate opening the restaurant."""
        print(f"{self.name} is now open!");

    def readNumberServed(self):
        """Print a statement showing the number of customers served."""
        print(f"{self.name} has served {self.numberServed} customers.");

    def setNumberServed(self, number):
        """Set the number of customers that have been served."""
        self.numberServed = number;

    def incrementNumberServed(self, additionalServed):
        """Add the given amount to the number of customers served."""
        self.numberServed += additionalServed;

myRestaurant = Restaurant('Pizza Hut', 'Italian');
myRestaurant.describeRestaurant();
myRestaurant.openRestaurant();

yourRestaurant = Restaurant('Chancellors', 'American');
yourRestaurant.describeRestaurant();
yourRestaurant.openRestaurant();

theirRestaurant = Restaurant('Sushi Boss', 'Japanese');
theirRestaurant.describeRestaurant();
theirRestaurant.openRestaurant();

myNewRestaurant = Restaurant('Homeward Bound', 'Southern Fusion');
myNewRestaurant.describeRestaurant();
myNewRestaurant.openRestaurant();

myNewRestaurant.numberServed = 10;
myNewRestaurant.readNumberServed();
myNewRestaurant.numberServed = 25;
myNewRestaurant.readNumberServed();

myNewRestaurant.setNumberServed(100);
myNewRestaurant.readNumberServed();

myNewRestaurant.incrementNumberServed(100);
myNewRestaurant.readNumberServed();
