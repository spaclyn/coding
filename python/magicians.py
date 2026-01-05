magicians = ['alice', 'david', 'carolina'];
for magician in magicians:
    print(magician);

sorcerers = ['dr.strange', 'gandalf', 'merlin'];
for sorcerer in sorcerers:
    print(f"{sorcerer.title()}, that was a great trick!");
    print(f"I can't wait to see your next trick, {sorcerer.title()}.\n");

print("Thank you, everyone. That was a great magic show!");

#slicing a list of magicians
print("Here are the first three magicians on my list:");
for magician in magicians[:3]:
    print(magician.title());
print("\nHere are the last two magicians on my list:");
for magician in magicians[-2:]:
    print(magician.title());
print("\nHere are the middle three magicians on my list:");
for magician in magicians[1:4]:
    print(magician.title());