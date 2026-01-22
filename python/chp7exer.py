#movie tickets
prompt = "\nHow old are you?"
prompt += "\n (enter 'exit' to quit.) "

while True:
    age = input(prompt)
    if age == 'exit':
        break

    age = int(age)
    if age < 3:
        ticketPrice = "free"
    elif age <= 12:
        ticketPrice = "10 dollars"
    elif age > 12:
        ticketPrice = "15 dollars"
    print(f"\tYour ticket will be {ticketPrice}.")



