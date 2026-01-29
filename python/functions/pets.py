def describePets(animalType , petName):     #a arguement with a default value cannot be followed by a arguement without a default value 
    """Display information about a whole pet"""
    print(f"\nI have a {animalType}")
    print(f"My {animalType}'s name is {petName.title()}.")

describePets('hamster', 'harry')
describePets(animalType = 'dog', petName = 'Fido')

