bicyles = ["trek", "cannondale", "redline", "specialized"];
print(bicyles)

#accessing elements in a list
print(bicyles[0]); #prints the 1st element; python uses 0-based indexing
print(bicyles[1].title()); #prints the 2nd element with the first letter capitalized
print(bicyles[2].upper()); #prints the 3rd element in uppercase
print(bicyles[-1]); #print the last element in the list, this is called negative indexing.

#using f-strings to print a message with an element from the list
message = f"Claudette's first bycycle was a {bicyles[1].title()}."
print(message)