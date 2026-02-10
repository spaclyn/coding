def getFormattedName(firstName, lastName):
    """Return a full name, neatly formatted."""
    fullName = f"{firstName} {lastName}"
    return fullName.title()
#This is an infinite loop!! why: because there is no quit condition
"""while True:
    print("\nPlease tell me your name:")
    fName = input("First Name: ")
    lName = input("Last Name: ")

    theformattedName = getFormattedName(fName, lName)
    print(f"\nHello, {theformattedName}!") """

while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")

    fName = input("First Name: ")
    if fName == 'q':
        break
    lName = input("Last Name: ")
    if lName == 'q':
        break

    theFormattedName = getFormattedName(fName, lName)
    print(f"\nHello, {theFormattedName}!")

musician = getFormattedName('jimi', 'hendrix')
print(musician)

def formattedName(firstName, middleName, lastName):
    """Return a full name, neatly formatted, with or without a middle name."""
    if middleName:
        fullName = f"{firstName} {middleName} {lastName}"
    else:
        fullName = f"{firstName} {lastName}"
    return fullName.title()

author = formattedName('Clive', 'Francis', 'Barker')
musician2 = formattedName('Beyonce','','Knowles-Carter');
# author2 = formattedName(firstName="JRR", lastName="Tolkien")      this doesnt work because there is no definited middleName arguement
print(author)
print(musician2)

  
