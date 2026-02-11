def greetUsers(names):
    """Prints a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!";
        print(msg);

usernames = ['hannah', 
             'ty',
             'margot'];
greetUsers(usernames);