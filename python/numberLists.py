#counting to twenty
for number in range(1, 21):
    print(number);

#One million number list
million = list(range(1, 1000001));
#print(million); # Uncommenting this line will print all numbers from 1 to 1,000,000. we really don't want to do that!

#summing a million numbers 
sum(million);
min(million);
max(million);
print(f"Minimum number in the list: {min(million)}");
print(f"Maximum number in the list: {max(million)}");
print(f"Sum of all numbers in the list: {sum(million)}");

#odd numbers from 1 to 20 
oddNumbers = list(range(1, 21, 2));
print("Odd numbers from 1 to 20:");
for number in oddNumbers:
    print(number);

# multiples of 3 from 3 to 30
multiplesThree = list(range(3, 31, 3));
print("Multiples of 3 from 3 to 30:");
for number in multiplesThree:
    print(number);

#cube comprehension
cubes = [value**3 for value in range(1, 11)];
print("Cubes of numbers from 1 to 10:");
for cube in cubes:
    print(cube);
print(cubes);