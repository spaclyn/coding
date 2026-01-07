cars = ['audi', 'bmw', 'subaru', 'toyota'];

for car in cars:
    if car == 'bmw':
        print(car.upper());
    else:
        print(car.title());

#toppings
requested_toppings = 'mushrooms';

if requested_toppings != 'anchovies':
    print("Hold the anchovies!");

#magic number
answer = 17;
if answer != 42:
    print("That is not the correct answer. Please try again!");

#magic number using input
#answer wouldnt work anyway because input() returns a string. so I needed to correct it but converting answer variable to int.
answers = input("What is the magic number? ");
answers = int(answers);

if answers != 42:
    print("That is not the correct answer. Please try again!");
else:
    print("Congratulations! You guessed the correct answer.");

#practice
car = 'subaru';
print("Is car == 'subaru'? I predict True.");
print(car == 'subaru');

print("\nIs car == 'audi'? I predict False.");
print(car == 'audi');

name = 'Claudette';
print("\nIs name == 'Claudette'? I predict True.");
print(name == 'Claudette');

print("\nIs name == 'Diana'? I predict False.");
print(name == 'Diana');

number = 10;
print("\nIs number == 10? I predict True.");
print(number == 10);

print("\nIs number == 5? I predict False.");
print(number == 5);

fruit = 'apple';
print("\nIs fruit == 'apple'? I predict True.");
print(fruit == 'apple');

print("\nIs fruit == 'banana'? I predict False.");
print(fruit == 'banana');