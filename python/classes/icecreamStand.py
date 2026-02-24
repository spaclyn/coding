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

class iceCreamStand(Restaurant):
    """A simple attempt to model an ice cream stand."""

    def __init__(self, resturantName, cuisineType):
        super().__init__(resturantName, cuisineType)
        self.flavors = [];
    
    def describeRestaurant(self):
        """Simulate Describe the resturant."""
        print(f"{self.name} serves {self.cuisineType}.");

    def addFlavor(self, flavor):
        """add a flavor to the list of flavors."""
        self.flavors.append(flavor);

    def displayFlavors(self):
        """DIsplay the Flavors that the ice cream stand offers."""
        print(f"{self.name} offers the following flavors: ");
        for flavor in self.flavors:
            print(f"- {flavor}");

myIceCreamStand = iceCreamStand('Scoops', 'Ice Cream');
myIceCreamStand.describeRestaurant();
myIceCreamStand.addFlavor('Vanilla');
myIceCreamStand.addFlavor('Chocolate');
myIceCreamStand.addFlavor('Strawberry');
myIceCreamStand.addFlavor('Mint Chocolate Chip');
myIceCreamStand.displayFlavors();