from pathlib import Path;

path = Path('python/exceptions/pi_digits.txt');
contents = path.read_text();

lines = contents.splitlines();
piString = '';
for line in lines:
    piString += line.lstrip(); #should remove the leading spaces in each line, but not trailing. i dont think there are any trailing spaces, but just in case.

print(piString);
print(len(piString));