age = 12
if age < 4: 
    print("Your admission cost is $0.");
elif age < 18:
    print("Your admission cost is $25.");
else:
    print("Your admission cost is $40.");

# using a variable to store price with narrowed down conditions
month = 1
if month in [3, 4, 5]:
    season = "Spring";
elif month in [6, 7, 8]:
    season = "Summer";
elif month in [9, 10, 11]:
    season = "Fall";
else:
    season = "Winter";

print(f"The season is {season}.");
#at first I thought to use ${season} in the f-string but that would not work since season is a string not a number.

# using multiple elif statements
day = "Saturday"
print (f"Today is {day}.")
if day == "Monday":
    print("It's the start of the work week.");
elif day == "Wednesday":
    print("We're halfway through the week!");
elif day == "Friday":
    print("The weekend is almost here!");
elif day == "Saturday" or day == "Sunday":
    print("It's the weekend, time to relax!");
else:
    print("It's a regular weekday.");

# using multiple conditions with logical operators
age = 12
if age < 4:
    price = 0;
elif age < 18:
    price = 25;
elif age < 65:
    price = 40;
elif age >= 65:
    price = 20;

print(f"Your admission cost is ${price}.");

#more practice
requestedTops = ['mushrooms', 'extra cheese'];
if 'mushrooms' in requestedTops:
    print("Adding mushrooms.");
if 'pepperoni' in requestedTops:
    print("Adding pepperoni.");
if 'extra cheese' in requestedTops:
    print("Adding extra cheese.");
print("\nFinished making your pizza!");

#more toppings
requestedToppings = ['mushrooms', 'green peppers', 'extra cheese', 'pepperoni'];
for requestedTopping in requestedToppings:
    if requestedTopping == 'green peppers':
        print("Sorry, we are out of green peppers right now.");
    else:
        print(f"Adding {requestedTopping}.");
print("\nFinished making your pizza!");

#checking that a list is not empty
requestedToppings = [];
if requestedToppings:
    for requestedTopping in requestedToppings:
        print(f"Adding {requestedTopping}.");
    print("\nFinished making your pizza!");
else:
    print("Are you sure you want a plain pizza?");

#using multiple lists
availableToppings = ['mushrooms', 'olives', 'green peppers', 
                     'pepperoni', 'pineapple', 'extra cheese'];
requestedToppings = ['mushrooms', 'french fries', 'extra cheese'];
for requestedTopping in requestedToppings:
    if requestedTopping in availableToppings:
        print(f"Adding {requestedTopping}.");
    else:
        print(f"Sorry, but we don't offer {requestedTopping} on pizza.");
print("\nFinished making your pizza!");