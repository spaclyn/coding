from pathlib import Path

path = Path('python/exceptions/pi_digits.txt');
contents = path.read_text().rstrip(); #moved the rstrip() here to remove the white space immediately, this is more efficicent 
#contents = contents.rstrip(); #removes white space, but might not be necessary in new versions of python
print(contents);

