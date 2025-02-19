#Guess the Number Game
'''The program generates a random number between 1 and 100.
The user has to guess the number.
For each guess:
Print "Too high!" if the guess is too high.
Print "Too low!" if the guess is too low.
Print "Congratulations! You guessed the number!" if the guess is correct.
Keep looping until the user guesses the number.'''

import random
while True:
    n=int(input("Guess the number: "))
    a=random.randint(1, 100)
    if n==a:
        print("Congratulations! You guessed the number!")
        break
    elif n>a:
        print("Too high, Guess again!")
    elif n<a:
        print("Too low, Guess again!")
    



