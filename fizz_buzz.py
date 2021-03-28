explain_game = (input("Have you played fizz buzz before?\n"))
if explain_game.lower() == "yes":
    print ("Okay, let's start.\n")
else:
    print ("Enter a number. If it's divisible by 3, I'll say fizz. If it's divisible by 5, I'll say buzz. If it's divisble by both I'll say fizz buzz.")

while True:
    number = int(input("Enter your number."))
    if number %3 == 0 and number %5 ==0:
        print("fizz buzz")
    elif number %3 == 0:
        print("fizz")
    elif number %5 == 0:
        print("buzz")
    else:
        print(number)
        
    play_again = input("Would you like to play again?\n")
    if play_again.lower() != "yes":
        break