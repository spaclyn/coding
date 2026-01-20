#a person I know
person0 = {
    'firstName':'Sebastian',
    'lastName':'Stan',
    'City': 'New York',
    }
person1 = {
    'firstName':'Tom',
    'lastName':'Hiddleston',
    'City': 'London',
}
person2 = {
    'firstName':'Troy',
    'lastName':'Baker',
    'City': 'Long Beach',
}

people = [person0, person1, person2]
for person in people:
    print(person)

pets = {
    'Stan': {
        'type':'Bird',
        'owner': 'Gabby',
    },
    'Tom': {
        'type':'Dog',
        'owner': 'Nene',
    },
    'Alpine': {
        'type':'Cat',
        'owner': 'James',
    },
}

for pet, petInfo in pets.items():
    print(f"\nThis is {pet}")
    petType = f"They are a {petInfo['type']}"
    ownerName = petInfo['owner']

    print(f"{petType}")
    print(f"Their owner is {ownerName}")



print(f"The person I like is named {person0['firstName']} {person0['lastName']}, and he lives in {person0['City']}");

#favorite number 
favNumbers = {
    'Jan': [5, 6, 7],
    'Nana': [11, 20],
    'Hero': [2, 0],
    'Goob': [99, 11],
    'Atiyah': [3, 13],
    }

print(f"Favrite Number list: {favNumbers}")
# iterative?
# to iterate over all values simulantously: dictName.keys()
# to iterate over just keys you would do: dictName.keys()
# to iterate over just values you would do: dictName.values()
for name, numbers in favNumbers.items():
    print(f"\n{name.title()}'s favorite number is:")
    for number in numbers:
        print(f"\t{number}")

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
