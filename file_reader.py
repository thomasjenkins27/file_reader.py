from pathlib import Path

path = Path("pi_million_digits.txt")

#Check to see if the path above exists
if path.exists():
    print("✅ File exists!")
else:
    print("❌ File does NOT exist!")

#If exists read the file
contents = path.read_text()

#Store each line of digits in a list.
lines = contents.splitlines()

#Create a variable called pi_string.
pi_string = ''

#For loop adds each line of digits to pi_string.
#Strip the extra white space from the left side of each line.
for line in lines:
    pi_string += line.lstrip()

#Print first 52 digits of the million pi numbers.
print(f"{pi_string[:52]}")
#Show length of string
print(len(pi_string))
