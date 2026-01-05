dimensions = (200, 50);
print(dimensions[0]);  # Output: 200
print(dimensions[1]); # Output: 50

#dimensions[0] = 250;  # This will raise a TypeError because tuples are immutable

for dimension in dimensions:
    print(dimension); #loops 

#reassigning a tuple
print("Original dimensions:");
for dimension in dimensions:
    print(dimension);

dimensions = (400, 100);
print("\nModified dimensions:");
for dimension in dimensions:
    print(dimension);

#buffet
buffet = ('spring rolls', 'dumplings', 'fried rice', 'noodles', 'sweet and sour pork');
print("Original buffet menu:");
for food in buffet:
    print(food);

#buffet[0] = 'egg rolls';  # This will raise a TypeError because tuples are immutable

#reassigning the buffet tuple
buffet = ('egg rolls', 'dumplings', 'fried rice', 'noodles', 'sweet and sour pork');
print("\nModified buffet menu:");
for food in buffet:
    print(food);


