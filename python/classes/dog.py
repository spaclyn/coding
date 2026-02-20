class Dog:
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
       """Initialize name and age attributes."""
       self.name = name
       self.age = age;
    
    def sit(self):
        """"Simulate a dog sitting in resposne to a command."""
        print(f"{self.name} is now sitting.");

    def rollOver(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!");

mydog = Dog('Pebbles', 3);
print(f"My Dog's name is {mydog.name}");
print(f"My Dog is {mydog.age} years old.");

mydog.sit();
mydog.rollOver();

yourDog = Dog('Button', 5);
print(f"Your Dog's name is {yourDog.name}");
print(f"Your Dog is {yourDog.age} years old.");
yourDog.sit();
yourDog.rollOver();

