#2-3. Personal Message
message = "Hello, {name}. Welcome to Python programming!";
name = "Claudette";
print(message.format(name=name));
# if we use print(message); it won't print the name variable in the message.
# but using the format() method allows us to insert the name variable into the message string.

#2-4. Name Cases
firstName = "Jeffrey";
lastName = "Landshark";
fullname = f"{firstName} {lastName}";
print(fullname.title());
print(fullname.upper());
print(fullname.lower());
# demonstrating title case, upper case, and lower case string methods

#2-5. Famous Quote
famousPerson = "J.R.R. Tolkien";
quote = 'Not all those who wander are lost.';
fullQuote = f'{famousPerson} once wrote, "{quote}"';
print(fullQuote);
# using double quotes around the quote to avoid syntax errors

#2-5-2. Famous Quote 2. no variable for famous person
print('J.R.R. Tolkien once wrote, "Not all those who wander are lost."');
# directly printing the quote without using a variable for the famous person

#2.6. Stripping Names
nameWithSpace = "  Claudette LaFevre  ";
print(nameWithSpace.lstrip());  # removes leading whitespace
print(nameWithSpace.rstrip());  # removes trailing whitespace
print(nameWithSpace.strip());   # removes both leading and trailing whitespace
# demonstrating lstrip(), rstrip(), and strip() string methods

#2.7 Syntax
url = "http://www.example.com/learnpython?ref=code";
print(url.removeprefix("http://"));  # removes the 'http://' prefix
print(url.removesuffix("?ref=code"));  # removes the '?ref=code' suffix
# demonstrating removeprefix() and removesuffix() string methods