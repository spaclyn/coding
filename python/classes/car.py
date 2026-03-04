# A class that can be used to represent a car.

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

myUsedCar = Car('suburu', 'Outback', 2015);
print(myUsedCar.getDescriptiveName());

myUsedCar.updateOdometer(23500);
myUsedCar.readOdometer();

myUsedCar.incrementOdometer(100);
myUsedCar.readOdometer();

myNewCar = Car('audi', 'a4', 2020);
print(myNewCar.getDescriptiveName());
myNewCar.odometerReading = 23;
myNewCar.updateOdometer(4000);
myNewCar.readOdometer();
