#cities
prompt = "\n Please enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you're finished.) "
cities = []


while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        cities.append(city)
        print(f"I'd love to go to {city.title()}!")

print(f"\nyour final list:")
for citi in cities:
    print(f"\t{citi}")