#Create a Python project of a Magic 8 Ball
#Allow the user to input their question.
#Show an in progress message.
#Create 10/20 responses, and show a random response.
#Allow the user to ask another question/advice or quit the game.

#1. Player needs to input a yes/no question
#2. Magic 8 Ball needs to give a random response (make 10 responses)
#3. Ask if user wants to ask another question or quit the game

import random

name=input ("Hello, what's your name?")
print("Welcome " + name + "!")

while True:
    question= input ("Please ask me a yes or no question.")
    answer= random.choice (["As I see it, yes.", "Ask again later.", "Don't count on it.", 
    "It is decidedly so.", "Better not tell you now.", "Very doubtful.", "You may rely on it.", 
    "Cannot predict now.", "My sources say no.", "Most likely."])
    print(answer)

    playagain= input("Do you require any further assistance, my child? Type yes or no.")

    if playagain.lower() != "yes":
        break



