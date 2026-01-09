alienColor = 'green'
if alienColor == 'green':
    print("You just earned 5 points!")
elif alienColor == 'yellow':
    print("You just earned 10 points!")
elif alienColor == 'red':
    print("You just earned 15 points!")

#stages of life
age = 65;
if age < 2:
    stage = "a baby";
elif age < 4:
    stage = "a toddler";
elif age < 13:
    stage = "a kid";
elif age < 20:
    stage = "a teenager";
elif age < 65:
    stage = "an adult";
else:
    stage = "an elder";
print(f"The person is {stage}.");