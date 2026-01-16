favLanguages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'erin': 'c',
    'maxwell': 'rust',
    'alexander': 'rust',
    'barbie': 'c sharp'
}

language = favLanguages['sarah'].title()
print(f"Sarah's favorite language is {language}");

print("\n")

#looping
for person, lang in favLanguages.items():
    print(f"{person.title()}'s favorite language is {lang.title()}!")

print("\n")

#new case
friends = ['jen', 'sarah']
for person in favLanguages.keys():
    print(f"Hi, {person.title()}")
    if person in friends:
        language = favLanguages[person].title()
        print(f"\tOh {person.title()}, I see you love {language}")
    elif 'erin' not in favLanguages.keys():
        print(f"Erin, Please take our poll Silly goose")

print("\n")

#sorting the keys 
for name in sorted(favLanguages.keys()):
    print(f"Hi {name.title()}, Thank's for taking the survey")

print("\n")

#values
print("The following languages have been mentioned:")
for language in favLanguages.values():
    print(f"{language.title()}")

print("\n")

#sets
print("Our language list with duplicates removed:")
for language in set(favLanguages.values()):
    print(f"{language.title()}")

