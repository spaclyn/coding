class User:
    """A Simple attempt to model a user."""

    def __init__(self, userName, eMail, firstName, lastName, age):
        """Initialize the user's attributes."""
        self.userName = userName;
        self.eMail = eMail;
        self.firstName = firstName;
        self.lastName = lastName;
        self.age = age;
    
    def describeUser(self):
        """Simulate describing the user."""
        print(f"\nGetting User Infomation for {self.userName.title()}...");
        print(f"User Information:");
        print(f"Username: {self.userName}");
        print(f"Email: {self.eMail}");
        print(f"First Name: {self.firstName}");
        print(f"Last Name: {self.lastName}");
        print(f"Age: {self.age}");

    def greetUser(self):
        """Simulate greeting the user."""
        print(f"Hello, {self.firstName.title()}! Welcome back!");

myUser = User('ajFlavors', 'aj@example.com', 'Aj', 'Ellerbee', 30);
myUser.describeUser();
myUser.greetUser();

yourUser = User('infiniteOne', 'satoruGoj@example.com', 'Satoru', 'Gojo', 28);
yourUser.describeUser();
yourUser.greetUser();

theirUser = User('godofWar', 'kratos@example.com', 'Kratos', 'Arkos', '1000');
theirUser.describeUser();
theirUser.greetUser();
