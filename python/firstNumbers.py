for value in range(1, 5):
    print(value); #we can see that this only prints number 1 to 4

for value in range(1, 6):
    print(value); #we can see that this prints number 1 to 5

range(6)  # this will create a range object from 0 to 5 

#using range() and list() to create a list of numbers from 0 to 5
numbers = list(range(1, 6));
print(numbers)  # Output: [1, 2, 3, 4, 5]

#using range() and list to print even numbers from 2 to 10
evenNumbers = list(range(2, 11, 2));
print(evenNumbers)  # Output: [2, 4, 6, 8, 10]

#squares of numbers from 1 to 10
squares = [];
for value in range(1, 11):
    square = value ** 2;
    squares.append(square);

print(squares);  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#using a more concise way to generate squares using list comprehension
squares = [];
for value in range(1, 11):
    squares.append(value**2);
print(squares);  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#using list comprehension to generate squares
squares = [value**2 for value in range(1, 11)];
print(squares);