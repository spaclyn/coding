def buildProfile(first, last, **userInfo):
    """Build a dictionary containing everything we know about a user."""
    userInfo['firstName'] = first
    userInfo['lastName'] = last
    return userInfo

def buildPerson(firstName, lastName, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': firstName, 'last': lastName}
    if age:
        person['age'] = age
    return person

def greetUser(username):
    """Displaying a simple greeting"""
    print(f"Hello, {username.title()}!")

def showMessages(messags):
    """Prints a serious of short messages."""
    for messag in messags:
        print(messag);