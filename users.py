userNames = ['admin', 'gameGuy123', 'proGamer', 'noobMaster69', 'eliteSniper', 'speedRunner'];
for userName in userNames:
    if userName == 'admin':
        print("Hello Admin, would you like to see a status report?");
    else:
        print(f"Hello {userName}, thank you for logging in again.");
if not userNames:
    print("We need to find some users!");

#com