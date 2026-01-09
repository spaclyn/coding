car = 'audi';

if car == 'bmw':
    print(car.upper());
else:
    print(car.title()); 

#toppings
requested_toppings = 'mushrooms';
if requested_toppings != 'anchovies':
    print("Hold the anchovies!");

#in my list
toppings = ['mushrooms', 'onions', 'pineapple'];
if 'mushrooms' in toppings:
    print("Adding mushrooms.");
if 'pepperoni' not in toppings:
    print("Pepperoni is not on the list.");

#numbers
answer = 17;
if answer != 42:
    print("That is not the correct answer. Please try again!");
if answer < 42:
    print("The answer is less than 42.");
if answer > 10:
    print("The answer is greater than 10.");
if answer <= 17:
    print("The answer is less than or equal to 17.");
if answer >= 15:
    print("The answer is greater than or equal to 15.");