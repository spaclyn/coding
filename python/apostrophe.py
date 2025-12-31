message = "It's a beautiful day in Apostrophe Land!";
print(message);

# note the use of double quotes to enclose a string that contains an apostrophe
# this prevents syntax errors that would occur if single quotes were used
# for example, the following would cause an error:
"""messageAgain = 'it's a beautiful day in Apostrophe Land!'; 
# print(messageAgain);"""
# this would cause a syntax error, so we use double quotes instead.

messageAgain = "It's another beautiful day in Apostrophe Land!";
print(messageAgain);
#or
messageAgain = 'It\'s another beautiful, wonderous day in Apostrophe Land!';
print(messageAgain);
# using backslash to escape the apostrophe when using single quotes