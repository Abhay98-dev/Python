#1. Basic if-else Conditions
'''1)Odd or Even:
Ask the user for a number and check if it is odd or even. Print the result.'''

num=int(input("Enter a number:"))
if num%2==0:
    print("Even")
else:
    print("Odd")

#2. Number Comparison
'''Ask the user for two numbers and determine which one is larger, or if they are equal.'''

num1=int(input("Enter first number:"))
num2=int(input("Enter Second Number:"))
if num1>num2:
    print(num1,"is larger than",num2)
elif num2>num1:
    print(num2,"is larger than",num1)
else:
    print("Both numbers are equal")

#3. Age Classification
'''Ask the user for their age and classify them based on the following criteria:

Age < 18: Print "You are a minor."
Age 18-64: Print "You are an adult."
Age 65+: Print "You are a senior citizen."'''

age=int(input("Enter your age:"))
if age<18:
    print("you are a minor")
elif age>=18 and age<=64:
    print("you are an adult")
else:
    print("you are a senior citizen")

#4 4. Simple Login Simulation
'''Ask the user to enter a username and password.

If the username is "admin" and the password is "password123", print "Access granted."
Otherwise, print "Invalid credentials."'''

username=input("Enter your username: ")
password=input("Enter your password:")
if username=="admin":
    if password=="password123":
        print("Access granted")
    else:
        print("Wrong password!")
else:
    print("wrong username")

#5.Grade Checker
'''Ask the user to input a grade percentage (0-100) and determine the letter grade using the following scale:

90-100: "A"
80-89: "B"
70-79: "C"
60-69: "D"
Below 60: "F"'''

per=int(input("enter your percentage: "))
if per>=90 and per<=100:
    print("A")
elif per>=80 and per<=89:
    print("B")
elif per>=70 and per<=79:
    print("C")
elif per>=60 and per<=69:
    print("D")
elif per<60:
    print("F")

#6. Leap Year Checker
'''Ask the user to input a year. Check if it is a leap year using the following rules:

A leap year is divisible by 4.
However, if it is divisible by 100, it must also be divisible by 400 to be a leap year.
Example:
Input: 2000
Output: "2000 is a leap year."'''

year=int(input("Enter a year: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,"is a leap year")

#7. Small Calculator
'''Ask the user for two numbers and an operation (+, -, *, /). Perform the operation and display the result.
If the user enters an invalid operation, print "Invalid operation."

Example:
Input: 5, 3, +
Output: "The result is 8."'''

n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
op=input("enter the operation: ")
if op=="+":
    print("the result is",n1+n2)
elif op=="-":
    print("the reult is",n1-n2)
elif op=="*":
    print("the result is",n1*n2)
elif op=="/":
    print("the result is",n1/n2)
else:
    print("Invalid operation")

#8. Traffic Light Decision
'''Ask the user for a traffic light color ("red", "yellow", "green") and print what they should do:

"red": Print "Stop."
"yellow": Print "Slow down."
"green": Print "Go."
Any other color: Print "Invalid color."'''

color=input("enter the trafic light colour: ")
if color=="red" or color=="Red":
    print("Stop")
elif color=="yellow" or color=="Yellow":
    print("slow down")
elif color=="green" or color=="Green":
    print("Go")
else:
    print("Invalid colour")
    