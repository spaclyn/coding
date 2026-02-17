#sandwhich practice
def buildSando(person, bread, **order):
    """Building a sandwhich order dictionary with person, bread, and other order details"""
    order['customer'] = person;
    order['bread'] = bread;
    return order

italiSando = buildSando('John Boyd', 'Subway bread', 
                        meat = 'Turkey', cheese = 'Provolone', 
                        veggies = 'Lettuce, Tomato, Onion', sauce = 'Mayo')
print(italiSando);

#meatballSub = buildSando('Jane Doe', 'Subway Break', topping = 'Extra Marinara Sauce')
#print(meatballSub)

#User Profile
def buildProfile(first, last, **userInfo):
    """Build a dictionary containing everything we know about a user."""
    userInfo['firstName'] = first
    userInfo['lastName'] = last
    return userInfo

myProfile = buildProfile('Atiyah', 'Ellerbee', location = 'Indiana', field = 'Computer Science', favoriteColor = 'Green');

#Cars
def buildCar(make, model, **carInfo):
    """Build a dictionary containing everything we know about a car."""
    carInfo['Make'] = make;
    carInfo['Model'] = model;
    return carInfo;

myCar = buildCar('Mazda', 'CX-5', color = 'Silver', year = 2014, mileage = 184300);
print(myCar);

car = buildCar('Suburu', 'Outback', color = 'Blue', towPackage = True);
print(car);