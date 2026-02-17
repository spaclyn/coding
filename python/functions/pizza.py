def makePizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings);

"""makePizza('pepperoni');
makePizza('mushrooms', 'green peppers', 'extra cheese');"""

#replacing print call with a lopp
def makePizzas(*toppings):
    """Print the list of toppings that have been requested."""
    print("Making a pizza with the following toppings: ");
    for topping in toppings:
        print(f"- {topping}");

"""makePizzas('pineapple');
makePizzas('olives', 'feta cheese', 'spinach');
"""

def makeMorePizzas(size, *toppings):
    """Sumarize the pizzas we will make"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ");
    for topping in toppings:
        print(f"- {topping}");

"""makeMorePizzas(12, 'black olives')
makeMorePizzas(16, 'green peppers', 'feta cheese', 'tomatoes')"""