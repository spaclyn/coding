alien0 = {'color': 'green', 'points': 5}
alien1 = {'color': 'yellow', 'points': 10}
alien2 = {'color': 'red', 'points': 15}

aliens = [alien0, alien1, alien2]

for alien in aliens:
    print(alien)

#modern example
aliens = []
for alienNum in range(30):
    newAlien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(newAlien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien ['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

#show first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

#show how many aliens were created
print(f"Total number of alines: {len(aliens)}")
