# Start with users that need to be verified,
# and an empty list to hold confirmed users.

unconfirmedUsers = ['alice', 'brian', 'candace']
confirmedUsers = []

# Verify each user until therea re no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmedUsers:
    currentUser = unconfirmedUsers.pop()

    print(f"Verifying User: {currentUser.title()}")
    confirmedUsers.append(currentUser)

#display all confirmed users.
print("\nThe Following users have been confirmed: ")
for confirmedUser in confirmedUsers:
    print(confirmedUser.title())

print("\n")

#removing all instances from a list 
pets = ['dog', 'cat', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

print("\n")

#deli exercise
sandwichOrder = ['Italian sub', 'Tuna sandwich', 'Meatball sub', 'Perscuttio Sando']
finishedSandos = []

while sandwichOrder:
    finishedSando = sandwichOrder.pop()

    print(f"\nI made a {finishedSando.title()} today.")
    finishedSandos.append(finishedSando)

#deli exercise
sandwichOrder = ['italian sub', 'tuna sandwich', 'pastrami sandwich', 'meatball sub', 'perscuttio sando', 'pastrami sandwich', 'Meatball sub', 'tuna sandwich', 'pastrami sandwich']
print(sandwichOrder)
print("\nWe are out of Pastrami today.")
finishedSandos = []

while sandwichOrder:
    while 'pastrami sandwich' in sandwichOrder:
        sandwichOrder.remove('pastrami sandwich')
    finishedSando = sandwichOrder.pop()

    print(f"\nI made a {finishedSando.title()} today.")
    finishedSandos.append(finishedSando)
print(finishedSandos)

#Dream Vacation
responses = {}
vacayPoll = True

while vacayPoll:
    name = input("\nWhat's your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    responses[name] = response
    repeat = input("Do you want to let someone else go next? (yes / no) ")
    if repeat == 'no':
        vacayPoll = False
print("\n --- Poll Results ---")
for name, response in responses.items():
    print(f"{name}'s dream vacation is to visit {response}")