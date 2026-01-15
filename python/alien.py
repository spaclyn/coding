alien0 = {'color': 'green', 'points': 5}
print(alien0['color']);
print(alien0['points']);

newPoints = alien0['points'];
print(f"You just got {newPoints} points")

alien0['xPosition'] = 0
alien0['yPosition'] = 25
print(alien0)

alien1 = {};

alien1['color'] = 'green'
alien1['points'] = 5
print(alien1)
#   I can print alien1's color like this if i wanted to 
# -> alien1Color = alien1['color']
# -> print(f"Our new alien is the color: {alien1Color}")
print(f"Our new alien's color is {alien1['color']}");

#changing alien color
alien1['color'] = 'yellow';
print(f"The new alien's is now {alien1['color']}");

# Tracking movement
alien1 = {'xPosition': 0, 'yPosition': 25, 'speed': 'fast'};  # dictionary keys are case sensitive.
print(f"The original position: {alien1['xPosition']}, {alien1['yPosition']}")

# Move Alien to the right
# Determine how far to move the alien based on it's current speed
if alien1['speed'] == 'slow':
    xIncrement =  1;
elif alien1['speed'] == 'medium':
    xIncrement = 2;
else: 
    #this must be a really fast alien
    xIncrement = 3;

#the new position would be the old position plus the increment.
alien1['xPosition'] = alien1['xPosition'] + xIncrement;
print(f"New Position: {alien1['xPosition']}");

#removing key-value pairs
del alien0['points']
print(alien0)

