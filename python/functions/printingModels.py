#start with some  designs that need to be printed.
unprintedDesigns = ['phone case', 'robot pendant', 'dodecahedron'];
completedModels = [];

#simulate printing each design, until none are left.
# move each design to completedModels after printing.
while unprintedDesigns:
    currentDesign = unprintedDesigns.pop();
    print(f"Printing model: {currentDesign}");
    completedModels.append(currentDesign);

# display all completed models.
print("\nThe following models have been printed: ");
for completedModel in completedModels:
    print(completedModel);


def printModels(unprintedDesigns, completedModels):
    """Simulate printing each design, until none are left.
    Move each design to completedModels after printing."""
    while unprintedDesigns:
        currentDesign = unprintedDesigns.pop();
        print(f"Printing model: {currentDesign}");
        completedModels.append(currentDesign);

def showCompletedModels(completedModels):
    """Show all the models that were printed."""
    print("\nThe following models have been printed: ");
    for completedModel in completedModels:
        print(completedModel);

printModels(unprintedDesigns[:], completedModels);
showCompletedModels(completedModels)