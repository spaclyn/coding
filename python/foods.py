myFoods = ['pizza', 'falafel', 'carrot cake']
friendsFoods = myFoods[:]

print("My favorite foods are:")
print(myFoods)

print("\nMy friend's favorite foods are:")
print(friendsFoods)

myFoods.append('cannoli')
friendsFoods.append('ice cream')

print("\nAfter adding new foods, my favorite foods are:");
for food in myFoods:
    print(f"- {food}");

print("\nAfter adding new foods, my friend's favorite foods are:");
for food in friendsFoods:
    print(f"- {food}");
