#rental
openCars = ['Suburu', 'Lincoln', 'Nissan']
wrentalCar = input("Please let me know what rental brand you would like? ").lower()
print(f"Okay lets try to find you a {wrentalCar.title()}...")

checkList = [item.lower() for item in openCars]
if wrentalCar in checkList:
    print(f"\tWe found you a {wrentalCar.title()}")
else:
    print(f"\tSorry We don't have a {wrentalCar.title()} avaliable.")
print("\n")

#returant seating
groupNum = input("Welcome, how many people are in your group? ")
groupNum = int(groupNum)

print(f"So {groupNum} people, then? Let's see if we can accomdate that...")
if groupNum <= 8:
    print(f"\tWe have a table for you, right this way!")
else:
    print(f"\tSorry guys, you will have to wait to be seated.")

print("\n")
#Evens or odds
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\n This number is EVEN")
else: 
    print(f"\n This number is ODD")

#multiple of 10
multi10 = input("Enter a number and I'll let you know if it's a multiple of 10: ")
multi10 = int(multi10)
if multi10 % 10 == 0:
    print(f"\tThis IS a multiple of 10")
else:
    print(f"\tThis IS NOT a multiple of 10")