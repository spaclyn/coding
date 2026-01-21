favPlaces = {
    'Nancy': ['London', 'France'],
    'Robert': ['Indiana', 'Indonesia'],
    'Rani': ['Canada', 'Yugoslavia'],
    'Ben': ['Halifax'],
}

for person, places in favPlaces.items():
    if len(places) == 1:
        print(f"\n{person.title()}'s favorite place is:")
        for place in places:
            print(f"\t{place.title()}")
    else:
        print(f"\n{person.title()}'s favorite places are:")
        for place in places: 
            print(f"\t{place.title()}")

cities = {
    'London': {
        'Country': 'England',
        'Population': '9 million',
        'Landmark': 'Eye of London'
    },
    'Paris': {
        'Country': 'France',
        'Population': '2.05 million',
        'Landmark': 'Eiffel Tower',
    },
    'Tokyo': {
        'Country': 'Japan',
        'Population': '41 million',
        'Landmark': 'Tokyo Tower',
    },
}

for place, placeInfo in cities.items():
    print(f"\nThis is {place.title()}! Here are some cool facts about {place.title()}:")
    popu = placeInfo['Population']
    countri = placeInfo['Country']
    landm = placeInfo['Landmark']
    print(f"\t{place.title()} is in {countri.title()}, with a population of {popu.upper()}, and it's home to the {landm.title()}")
