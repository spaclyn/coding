import masterFunctions as mf

musician = mf.buildPerson('Jimi', 'Hendrix', age=27)
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