class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make;
        self.model = model;
        self.year = year;
        self.odometerReading = 0;

    def getDescriptiveName(self):
        """Return a neatly formatted descriptive name."""
        longName = f"{self.year} {self.make} {self.model}"
        return longName.title();

    def readOdometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometerReading} miles on it.");

    def updateOdometer(self, mileage):
        """Set the odometer reading to the given value.
        Update: Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometerReading:
            self.odometerReading = mileage;
        else:
            print("You can't roll back an odometer!");

    def incrementOdometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometerReading += miles;

class ElectricCar(Car):
    """Represents aaspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year);
        self.batterySize = 40;

    def describeBattery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.batterySize}-kWh battery.");

    #def fillGasTank(self):

myLeaf = ElectricCar('nissan', 'leaf', 2024);
print(myLeaf.getDescriptiveName());
myLeaf.describeBattery();
