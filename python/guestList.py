#making list of guests to invite to dinner
guestList = ['Loki Laufeyson', 'Jeff The Landshark', 'Bruce Wayne', 'Diana Prince'];
print("Original Guest List:");
print(guestList);

#sending invitations
for guest in guestList:
    invitation = f"Dear {guest.title()}, you are cordially invited to dinner at my place this Saturday evening. Looking forward to your presence!";
    print(invitation);

#we find out that bruce wayne cannot make out it to dinner
print("\nUnfortunately, Bruce Wayne cannot make it to dinner.");
#replacing bruce wayne with tony stark
guestList[2] = 'tony stark';
print("\nUpdated Guest List:");
print(guestList);

print("\nSending updated invitations:");
for guest in guestList:
    invitation = f"Dear {guest.title()}, you are cordially invited to dinner at my place this Saturday evening. Looking forward to your presence!";
    print(invitation);

#we found a bigger dinner table, so we can invite more people
print("\nGood news! We found a bigger dinner table, so we can 3 more guests.");
#adding a guest to the beginning of the list
guestList.insert(0, 'Steve Rogers');
guestList.insert(2, 'Stephen Shannon Strange');
guestList.append('Claudette LaFevre');
print("\nExpanded Guest List:");
print(guestList);

print("\nSending new invitations to all guests:");
for guest in guestList:
    invitation = f"Dear {guest.title()}, our party has grown! You are still cordially invited to dinner at my place this Saturday evening. Looking forward to your presence!";
    print(invitation);

#unfortunately, the new dinner table will not arrive on time, and we can only invite 2 people for dinner
print("\nUnfortunately, the new dinner table will not arrive on time, and I can only invite 2 people for dinner.");
while len(guestList) > 2:
    removed_guest = guestList.pop();
    apology = f"Dear {removed_guest.title()}, I regret to inform you that due to unforeseen circumstances, I can no longer accommodate you for dinner this Saturday. My sincerest apologies. Lets hang out another time!";
    print(apology);
print("\nFinal Guest List:");
print(guestList);

#sending final invitations to the remaining guests
for guest in guestList:
    final_invitation = f"Dear {guest.title()}, you are still invited to dinner at my place this Saturday evening. Looking forward to your presence!";
    print(final_invitation);

#removing the last 2 guests to empty the list
del guestList[0];
del guestList[0];
print("\nGuest List after removing all guests:");
print(guestList);