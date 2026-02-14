def buildProfile(first, last, **userInfo):
    """Build a dictionary containing everything we know about a user."""
    userInfo['firstName'] = first
    userInfo['lastName'] = last
    return userInfo

userProfile = buildProfile('albert', 'einstein',
                           location = 'princeton',
                           field = 'physics')

print(userProfile)