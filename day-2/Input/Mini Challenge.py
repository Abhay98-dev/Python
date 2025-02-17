#Create a small program that: 1. Asks the user for their full name. 2. Splits the name into first and last names. 3. Prints the initials in uppercase

name=input("enter your full name:")
n=name.split()
first=n[0]
last=n[1]
print(first[0].upper()+"."+last[0].upper())