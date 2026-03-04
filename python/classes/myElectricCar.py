from car import ElectricCar

myLeaf = ElectricCar('nissan', 'leaf', 2024);
print(myLeaf.getDescriptiveName());
myLeaf.battery.describeBattery();
myLeaf.battery.getRange();
myLeaf.fillGasTank();