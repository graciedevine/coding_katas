import random


def play_game():
    guesses = 0
    number = random.randint(1, 10)

    while guesses < 3:
        guess = int(input("I'm thinking of a number between 1 and 10.\n"))
        guesses = guesses + 1

        if guess < number:
            print("Guess higher!")
        elif guess > number:
            print("Guess lower!")
        else:
            print("That's right! You got it!")
            break

    if guess != number:
        print("Sorry, the number I was thinking of was " + str(number))


play_game()
