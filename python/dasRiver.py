rivers = {
    'nile': 'egypt',
    'thames': 'england',
    'amazon': 'south america'
}

for river, country in rivers.items():
    print(f"the {river.title()} is a river in {country.title()}")

print("\nAll of my Rivers:")
for river in sorted(rivers.keys()):
    print(f"\t{river.title()}")

print("\nAll of my Origins:")
for country in sorted(rivers.values()):
    print(f"\t{country.title()}")

#polling
favRivers = {
    'jen': 'nile',
    'sarah': 'thames',
    'edward': 'nile',
    'phil': 'nile',
    'erin': 'amazon',
}

takePoll = ['jen', 'phil', 'sarah', 'erin', 'martha', 'barbie']

#right one
for person in takePoll:
    if person in favRivers.keys():
        print(f"{person}, Thanks for taking the poll!")
    else:
        print(f"Hey {person}, you should take our poll.")
print("\n")

#this is a different usecase than what i was asked for.
# -> it is looking through people in favRivers keys instead of the other way around
# -> so instead of using favRivers as a reference for people who have taken the poll, it uses takePoll
# -> this means edward is asked to take the poll because hers in takePoll even though you can clearly see he's already taken it
for people in favRivers.keys():
    if people in takePoll:
        print(f"{people}, Thanks for taking the poll")  
    else:
        print(f"Hey {people}, please take our poll")
