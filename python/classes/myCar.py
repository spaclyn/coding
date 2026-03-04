from car import Car

myNewCar = Car('audi', 'a4', 2020);
print(myNewCar.getDescriptiveName());
myNewCar.odometerReading = 23;
myNewCar.readOdometer();
myNewCar.updateOdometer(4000);