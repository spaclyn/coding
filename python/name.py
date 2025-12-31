"""
Docstring for name.py
"""

##Variable Formatting Examples and String Methods

#Title Case Example
name = "ada lovelace";
print(name.title());

#Additional examples; upper() and lower()
name2 = "Grace Hopper";
print(name2.upper());
name3 = "Alan Turing";
print(name3.lower());

#Using f-strings to format variables into messages
firstName = "Claudette";
lastName = "LaFevre";
fullName = f"{firstName} {lastName}";
lastFirst = f"{lastName}, {firstName}";

print(f"Hello, {fullName.title()}!");
print(f"Loading Profile for {lastFirst.upper()}...");
print(f"Greetings, {firstName.title()}!");