import random

print("Hello, What is your name?")
name = input()

print("Well " + name + " I am guessing a number between 1 to 20")

secretNum = random.randint(1, 20)

#Asking the player for maximum 6 guesses

for guessTaken in range(1,7):
    print("Take a Guess")
    guess = int(input())
    if guess < secretNum:
        print("Your guess is too low!")

    if guess > secretNum:
        print("Your guess is too high")

    else:
        break

if guess == secretNum:
    print("Congratulations " + name + "! You have guessed the correct number")
else:
    print("Nope! I was thinking of " + secretNum)