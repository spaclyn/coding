#sorting a list permenently using sort(), which sorts the list in alphabetical order by default
cars = ['bmw', 'audi', 'toyota', 'subaru'];
cars.sort();
print(cars);

#if you want reverse alphabetical order, you can pass the argument reverse = True
cars.sort(reverse=True);
print(cars);

#sorting a list temporarily using sorted(), which returns a new sorted list without changing the original
cars = ['bmw', 'audi', 'toyota', 'subaru'];
print("\nOriginal and Sorted() List:")
print(cars);
print(sorted(cars));

print("\nOriginal List after using sorted():")
print(cars);

#using reverse() to reverse the order of a list
cars = ['bmw', 'audi', 'toyota', 'subaru'];
print("\nOriginal List:");
print(cars);
cars.reverse();
print("Reversed List:");
print(cars);

