# 1) Basic Data Types
'''Q1)Create variables of the following types:
An integer 
A float 
A string 
A boolean 
Q2)Print the type of each variable.
'''

a=10
print("type of a is",type(a))

b=10.5
print("type of b is",type(b))

c="Hello World"
print("type of c is",type(c))

d=True
print("type of d is",type(d))


# 2. Type Casting
'''Convert an integer to a float.
Convert a float to an integer.
Convert a string  to an integer.
Convert a boolean  to an integer.
Print the results after each conversion.
'''

f=10.5
print(type(int(f)))

g="1234"
print(type(int(g)))

i=True
print(type(int(i)))

# 3. String Operations
'''Create a string variable with your name  and print its length using len().
Print the first letter of your name using slicing .
Print the last letter of your name using negative indexing.
Print the string in reverse order.
Concatenate two strings  and print the result.'''

name="Abhay"

print(len(name))

print(name[0])

print(name[-1])

print(name[::-1])

print("Hello, "+"World!")

#4. User Input
'''Ask the user for their name using the input() function and store it in a variable.
Ask for their age and store it in a variable.
Print a message like "Hello, [name]! You are [age] years old." using f-strings.'''

name1=input("enter your name:")
print(name1)

age=int(input("enter your age:"))

print("hello",name1,"you are",age,"years old")

#5. Challenge: Mini Program
'''Create a small program that:

Asks the user for their birth year.
Calculates their current age using the current year (you can hard-code the year as 2025 for now).
Prints the age using a message like "You are [age] years old.".'''

birth=int(input("enter your birth year:"))
current=2025
age=current-birth
print("you are",age,"years old")
