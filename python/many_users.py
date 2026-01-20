users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
        'mcurie': {
            'first': 'marie',
            'last': 'curie',
            'location': 'paris',
        },
}

for username, userInfo in users.items():
    print(f"\nUsername: {username}")
    fullName = f"{userInfo['first']} {userInfo['last']}"
    location = userInfo['location']

    print(f"\tFull name: {fullName.title()}")
    print(f"\tLocation: {location.title()}")
