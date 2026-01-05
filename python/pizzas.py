pizza = ['pepperoni', 'mushroom', 'ground beef', 'extra cheese'];
for topping in pizza:
    print(f"I like {topping} pizza!");

print("I really love pizza!");

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
