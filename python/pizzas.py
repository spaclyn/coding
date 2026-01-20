#pizza for dictionaries
pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese', 'pepperoni']
}

print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

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