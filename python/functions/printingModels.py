import printingFunctions as pf
#from printingFunctions import printModels, showCompletedModels

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


pf.printModels(unprintedDesigns[:], completedModels);
pf.showCompletedModels(completedModels)