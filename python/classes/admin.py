class User:
    """A Simple attempt to model a user."""

    def __init__(self, userName, eMail, firstName, lastName, age):
        """Initialize the user's attributes."""
        self.userName = userName;
        self.eMail = eMail;
        self.firstName = firstName;
        self.lastName = lastName;
        self.age = age;
        self.loginAttempts = 0;
    
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

    def incrementLoginAttempts(self):
        """Increment the value of loginAttempts."""
        self.loginAttempts += 1;

    def restLoginAttempts(self):
        """Reset loginAttempts to 0."""
        self.loginAttempts = 0;
    
    def readLoginAttempts(self):
        """Print a statement showing the number of login attempts."""
        print(f"{self.userName} has attempted to login {self.loginAttempts} times.");

class Admin:
    """Admin User"""

    def __init__(self, userName, eMail, firstName, lastName, age):
        """Initialize the admin user's attributes."""
        super().__init__(userName, eMail, firstName, lastName, age);
        self.privileges = [];

    def showPrivileges(self):
        """Show the admin's privileges."""
        print(f"{self.userName} has the following privileges: ");
        for privilege in self.privileges:
            print(f"- {privilege}");
