friends = ['Claudette', 'Jake', 'Meg', 'Dwight'];
print(friends)

# Accessing elements in a list
print(friends[1]) # should print 'Jake'
print(friends[2].upper()) # should print 'MEG'
print(friends[-1].title()) # should print 'Dwight'
print(friends[0].lower()) # should print 'claudette'

#Using Elements from friends to make personalized messages 
megMessage = f"{friends[2]}, have you finished track practice for today?";
print(megMessage);

claudMessage = f"{friends[0]}, did you speak with {friends[1]} today about your date?";
print(claudMessage);

dwightMessage = f"Will you order some pizza for us {friends[3]}?";
print(dwightMessage);

#random list and messages
brands = ['coach', 'nike', 'prada', 'michael kors'];
print(brands)

nikeMessage = f'Last Night, I brought a new pair of {brands[1].title()} sneakers.';
print(nikeMessage);
pradaMessage = f'I wish I could afford a vintage {brands[2].title()} handbag.';
print(pradaMessage);
michaelKMessage = f'My momma owns a {brands[3].title()} bag from the store downtown.';
print(michaelKMessage);
coachMessage = f'My first purse was a {brands[0].title()} bag, it was a gift from {friends[0].title()}.';
print(coachMessage);