motorcycles = ['honda', 'yamaha', 'suzuki', 'kawasaki'];
print("Original list of motorcycles:");
print(motorcycles);

#accessing and changing elements in the list
motorcycles[0] = 'ducati';  #changing the first element
print("\nList after changing the first motorcycle to 'ducati':");
print(motorcycles);

#adding using append()
motorcycles.append('bmw'); #adding 'bmw' to the end of the list
motorcycles.append('honda'); #adding 'honda' to the end of the list
print("\nList after appending 'bmw' and 'honda':");
print(motorcycles);

#append empty list
motorcycles2 = [];
motorcycles2.append('triumph');
motorcycles2.append('harley-davidson');
print("\nNew list after appending:");
print(motorcycles2);

#using insert() to add an element at a specific position
motorcycles2.insert(1, 'kawasaki'); #inserting 'kawasaki' at index 1
print("\nList after inserting 'kawasaki' at index 1:");
print(motorcycles2);

#using del to remove an element by index
del motorcycles2[2]; #removing the element at index 3
print("\nList after deleting the element at index 2:");
print(motorcycles2);

#but we can remember to access the last element of the list we use negative indexing, so its easier to remember this based on the length of the list.
del motorcycles[-1]; #removing the last element
print("\nList after deleting the last element:");
print(motorcycles);
#bye bye honda

#using pop() to remove an element and use it
popped_motorcycle = motorcycles.pop(); #removes the last element and stores it if popped.
print(motorcycles);
print(popped_motorcycle)

#Example use of pop() is printing something in chronological order. Since it pulls the last element, we can use it to print things in reverse order.
myCycles = ['honda', 'yamaha', 'suzuki'];
last_owned = myCycles.pop();
print(f"\nThe last motorcycle I owned was a {last_owned.title()}.");

#you can also pop from any position in the list by specifying the index
first_owned = myCycles.pop(0); #pops the first element
print(f"The first motorcycle I owned was a {first_owned.title()}.");

#using remove() to remove an element by value
motorcycles.remove('yamaha'); #removes 'yamaha' from the list
print("\nList after removing 'yamaha':");
print(motorcycles);

#using remove() to remove an element for a reason
too_ugly = 'ducati';
motorcycles.remove(too_ugly);
print(motorcycles);
print(f"\nA {too_ugly.title()} is too ugly for me!");
