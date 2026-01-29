def buildPerson(firstName, lastName, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': firstName, 'last': lastName}
    if age:
        person['age'] = age
    return person

musician = buildPerson('Jimi', 'Hendrix', age=27)
print(musician)

def cityCountry(city, country):
    """Defines City and Country"""
    countryCity = f"{city.title()}, {country.title()}"
    return countryCity
santiChile = cityCountry('santiago', 'Chile')
tokyJapan = cityCountry('Tokyo', 'japan')
washiUsa = cityCountry('Washington D.C', 'USA')
print(tokyJapan)
print(washiUsa)
print(santiChile)