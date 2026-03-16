from pathlib import Path

path = Path("python/exceptions/pi_million_digits.txt");
contents = path.read_text();

lines = contents.splitlines();
piString = '';
for line in lines:
    piString += line.lstrip(); #should remove the leading spaces in each line.

print(f"{piString[:52]}...");
print(f"Length of the string: {len(piString)}");
