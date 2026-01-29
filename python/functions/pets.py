def describePets(animalType , petName):     #a arguement with a default value cannot be followed by a arguement without a default value 
    """Display information about a whole pet"""
    print(f"\nI have a {animalType}")
    print(f"My {animalType}'s name is {petName.title()}.")

describePets('hamster', 'harry')
describePets(animalType = 'dog', petName = 'Fido')

def makeshirt(size, text):
    """Display information about a shirt"""
    print(f"\nYou have ordered a shirt of size {size} with the text '{text}' printed on it.")

makeshirt('L', 'Sweet Shirt');
makeshirt(size = 'L', text = "Shirt");

def makeLargeShirt(text, size = 'L'):
    """Display information about a large shirt"""
    print(f"\nYou have ordered a shirt of size {size} with the text '{text}' printed on it.")

