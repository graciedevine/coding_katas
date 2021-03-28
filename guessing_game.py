"""Practice exercise taken from w3resource.com.
Write a Python program to guess a number between 1-9.
User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit."""

#My code before looking for help. I attempted to put the whole thing in a while loop, but the break statement said it was outside bounds. When removing the while loop, "if guess != secret_number" only looped twice
#before quitting.

#import random

#guess = int(input("I'm thinking of a number between 1 to 9...\n"))

#secret_number = random.randint(1,9)

#while True:

#if guess != secret_number:
    #print (int(input("Sorry, guess again.\n")))

#if guess == secret_number:
    #print ("Congratulations.")


#Code I found in a video tutorial:

import random

number = random.randrange (1,9)

guess =  int(input("Guess a number between 1-9.\n"))

while guess != number:
    if guess < number:
        print ("Guess higher!")
        guess =  int(input("Guess a number between 1-9.\n"))

    else:
        print ("Guess lower!")
        guess =  int(input("Guess a number between 1-9.\n"))

print("Yes, that's it!")






        