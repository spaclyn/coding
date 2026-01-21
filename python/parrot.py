prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = " "
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)


#greeter.py
name = input("Please enter your name: ")
print(f"Hello, {name}") #Dont need a linebreak here, python automatically does that in terminal

prompt = "If you share your name, we can personalize the message you see."
prompt += "\n What is your first name? "
name = input(prompt)
print(f"Hello again, {name}")