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