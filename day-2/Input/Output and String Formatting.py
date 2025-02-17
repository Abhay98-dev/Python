#1. Basic Input/Output
'''Ask the user for their name and print a greeting message.
Ask the user for two numbers and print their sum.'''

name=input("enter your name:")
print("hello",name)

num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
print("sum of the given numbers is:",num1+num2)


#2. String Formatting with f-strings
'''Ask the user for their name, age, and city.
Print a message like:
"Hello, [name]! You are [age] years old and live in [city]."
Ask the user for the price of an item and a discount percentage.
Calculate the discounted price and print it with 2 decimal places using f-strings.'''

nam=input("enter your name:")
age=int(input("enter your age:"))
city=input("enter your city:")
print(f"hello {nam}! you are {age} years old and live in {city}")
price=float(input("enter the price of the item:"))
discount=float(input("enter the discount percentage:"))
dis=price-(price*(discount/100))
print(f"discounted price is {dis:.2f}")


#3. Basic Error Handling (try/except)
'''Ask the user to input two numbers.
If the user enters a non-numeric value, print a friendly error message.
If both inputs are valid, print their sum.
Ask the user for a number and divide 100 by that number.
Handle the case where the user enters 0 and print an error message (e.g., "Division by zero is not allowed!").'''

try:
    num1=int(input("enter first number:"))
    num2=int(input("enter the second number:"))
    print("sum of the given numbers is:",num1+num2)
except ValueError:
    print("please enter a numeric value")

try:
    num=int(input("enter a number:"))
    print(100/num)
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("please enter a numeric value")
