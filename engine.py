# This game about guess number
import random

guessTaken = 0

print("Hi! What's your name?")

myName = input()

number = random.randint(1, 20)  # guess the random number
print(f'Well, {myName} I`m choose number from 1 to 20.')

for guessTaken in range(6):
    print('Try to guess.')
    guess = int(input())

    if guess < number:
        print('Your number is smaller')

    if guess > number:
        print('Your number is biggest')

    if guess == number:
        break

if guess == number:
    guessTaken = str(guessTaken + 1)
    print(f'Well done {myName}! You guess the number at {guessTaken} try!')

if guess != number:
    number = str(number)
    print(f'Sorry! I`m guess the number {number}.')
