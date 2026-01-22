#pizza for dictionaries
"""
pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese', 'pepperoni']
}

print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")
"""

#user input for toppings 
pizzaTops = []
message = "\nWhat do you want on your pizza?"
message += "\n(Enter 'done' to exit.) "

while True:
    pizzaTop = input(message)
    if pizzaTop == 'done':
        break
    else:
        pizzaTops.append(pizzaTop)
        print(f"We'll add {pizzaTop} to your pizza")

print("\nHere are the toppings on your pizza:")
for toppings in pizzaTops:
    print(f"\t{toppings}")

"""pizza = ['pepperoni', 'mushroom', 'ground beef', 'extra cheese'];
for topping in pizza:
    return none
   print(f"I like {topping} pizza!");

#print("I really love pizza!");

friendsPizza = pizza[:]
friendsPizza.append('pineapple');
pizza.append('bbq chicken');
print("My favorite pizzas are:");
for p in pizza:
    print(f"- {p}");

print("\nMy friend's favorite pizzas are:");
for p in friendsPizza:
    print(f"- {p}");


## animals

animals = ['dog', 'cat', 'rabbit'];
for animal in animals:
    print(f"A {animal} would make a great pet.");

print("And any of these animals could have floppy ears!");
"""