from pathlib import Path

path = Path("python/exceptions/pi_million_digits.txt");
contents = path.read_text();

lines = contents.splitlines();
piString = '';
for line in lines:
    piString += line.lstrip(); #should remove the leading spaces in each line.

birthday = input("Enter your birthday, in the form mmddyy: ");
if birthday in piString:
    print("Your birthday appears in the first million digits in pi!");
else:
    print("Your birthday does not appear in the first million digits in pi.");
