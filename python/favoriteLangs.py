favLanguages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

language = favLanguages['sarah'].title()
print(f"Sarah's favorite language is {language}");

#looping
for person, lang in favLanguages.items():
    print(f"{person.title()}'s favorite language is {lang.title()}!")
