#1. Print Numbers from 1 to 10
for i in range(1,11):
    print(i)

#2. Sum of First N Natural Numbers
n=int(input("Enter a number:"))
sum=0
for i in range(1,n+1):
    sum+=i
print("The sum of first ",n," natural number is:",sum)

#3. Multiplication Table
num=int(input("Enter the number: "))
mul=1
for i in range(1,11):
    mul=i*num
    print(num,"*",i,"=",mul)

#4. Factorial of a Number
num1=int(input("Enter a number: "))
fact=1
for i in range(1,num1+1):
    fact*=i
print("Factorial of ",num1," is ",fact)

#5. Reverse a Given String
st=input("Enter a string: ")
rev=""
for i in range(len(st)-1,-1,-1):
    rev+=st[i]
print("The reverse of ",st," is ",rev)

#6. Count Vowels in a String
vow=input("Enter a string: ")
count=0
for i in vow:
    if i in "aeiouAEIOU":
        count+=1
print("The number of vowels in ",vow," is ",count)

#77. FizzBuzz
'''Print numbers from 1 to 20. For each number:

If divisible by 3, print "Fizz"
If divisible by 5, print "Buzz"
If divisible by both 3 and 5, print "FizzBuzz"
Otherwise, print the number itself.'''

for i in range(1,21):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

#8. Infinite Loop with Break
'''Create a while loop that runs infinitely but breaks when the user types "exit".'''
while True:
    a=input("press any key to continue or type exit to stop: ")
    if a=="exit" or a=="Exit":
        print("loop breaked")
        break
    else:
        print("i am alive")