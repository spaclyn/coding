
#starting my website with usernames
userNames = ['admin', 'gameGuy123', 'proGamer', 'noobMaster69', 'eliteSniper', 'speedRunner'];
for userName in userNames:
    if userName == 'admin':
        print("Hello Admin, would you like to see a status report?");
    else:
        print(f"Hello {userName}, thank you for logging in again.");
if not userNames:
    print("We need to find some users!");

#checking if usernames are unique
currentUsers = ['admin', 'gameGuy123', 'proGamer', 'noobMaster69', 'eliteSniper', 'speedRunner'];
newUsers = ['ProGamer', 'newUser1', 'speedrunner', 'gamerGirl', 'montyPy'];
Users = [item.lower() for item in currentUsers]; #this is an inline way of making the items lowercase by copying the list above.
for user in newUsers:
    if user.lower() in Users:
        print(f"The Username {user}, is taken")
    else:
        print(f"Welcome, {user}")

#Ordinal Numbers
numberList = [1,2,3,4,5,6,7,8,9]

for number in numberList:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')

#dictionary practice
user1 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for x,y in user1.items():
    print(f"\nKey: {x}")
    print(f"Value: {y}")