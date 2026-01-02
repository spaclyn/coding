places = ['paris', 'tokyo', 'new york', 'china', 'london'];
print(places);

#sorted() order
print("\nSorted List:");
print(sorted(places));

#original list remains unchanged
print("\nOriginal List after using sorted():");
print(places);

#reverse alphabetical order using sorted()
print("\nSorted List in Reverse Order:");
print(sorted(places, reverse=True));

print("\nOriginal List after using sorted() with reverse:");
print(places);

#using reverse() to reverse the order of the original list
places.reverse();
print("\nReversed Original List:");
print(places);

#sorting reverse again to restore original order
places.reverse();
print("\nRestored Original List:");
print(places);

#sort() to change to alphabetical order permanently
places.sort();
print("\nPermanently Sorted List:");
print(places);

#sort() to change to reverse alphabetical order permanently
places.sort(reverse=True);
print("\nPermanently Sorted List in Reverse Order:");
print(places);

#counting my dinner guests
guestList = ['Loki Laufeyson', 'Jeff The Landshark', 'Bruce Wayne', 'Diana Prince'];
print("Original Guest List:");
print(guestList);

len(guestList)
print(f"\nNumber of Guests Invited: {len(guestList)}");

#languages I want to learn
languages = ['python', 'javascript', 'c++', 'java', 'ruby', 'go'];
print("\nLanguages I Want to Learn:");
print(languages);

print(f"\nNumber of Languages I Want to Learn: {len(languages)}");
print(sorted(languages));
print(sorted(languages, reverse=True));

print("\nOriginal Languages List:");
print(languages);
languages.sort();
print("\nPermanently Sorted Languages List:");
print(languages);
languages.sort(reverse=True);
print("\nPermanently Sorted Languages List in Reverse Order:");
languages.reverse();
print("\nReversed Languages List:");
print(languages);