from masterFunctions import *;
messags = ["Hi Guys",
            "Who's ready to lean Python?",
            "Do you like programming? I do!"];


showMessages(messags);

greetings = ['Hey There',
             'Welcome to the World of Python',
             'Hello World']
showMessages(greetings);

def sendMessages(messages, sentMessages):
    """SImulate sending each message, until none left.
    Move each messae to sentMessages after sending/printing."""
    while messages:
        unsentMessage = messages.pop();
        print(f"Sending Message: {unsentMessage}");
        sentMessages.append(unsentMessage);

messages = ["Hi Guys",
            "Who's ready to lean Python?",
            "Do you like programming? I do!"];
sentMessages = [];
sendMessages(messages[:], sentMessages);
print(messages);
print(sentMessages);
