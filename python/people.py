#a person I know
person0 = {
    'firstName':'Sebastian',
    'lastName':'Stan',
    'City': 'New York',
    }

print(f"The person I like is named {person0['firstName']} {person0['lastName']}, and he lives in {person0['City']}");

#favorite number 
favNumbers = {
    'Jan': 5,
    'Nana': 20,
    'Hero': 2,
    'Goob': 99,
    'Atiyah': 3,
    }

print(f"Favrite Number list: {favNumbers}")
# iterative?
# to iterate over all values simulantously: dictName.keys()
# to iterate over just keys you would do: dictName.keys()
# to iterate over just values you would do: dictName.values()
for name, numb in favNumbers.items():
    print(f"{name}'s favorite number is {numb}")

#glossary
pyGlossary = {
    'variable': 'a is label that points to assigned information',
    'if-else statement': 'a statement chain that can handle use parameters',
    'elif': 'apart of if-else statements that can work between if and else parameters',
    'list': 'an array of items that are typically assigned and saved together, different from dictionary',
    'for loop': 'a loop that will iterate through a list or other iterable objects.',
    'dictionary': 'a array that takes key-value pairs together',
    'set': 'a set is not a dictionary. a set typically isn\'t a key-value pair',
    'constant': 'a variable that reamins unchanged, typically uppercase',
    'tuple': 'ordered and immutable objects, once created you cannot change them',
    'boolean': 'typically represent a truth value: true or false.'
}

for term, deff in pyGlossary.items():
    print(f"{term}: {deff}");
