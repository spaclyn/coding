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

myNewCar = Car('audi', 'a4', 2020);
print(myNewCar.getDescriptiveName());
myNewCar.readOdometer();
