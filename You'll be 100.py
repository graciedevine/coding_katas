#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime
name = input("What's your name?")
age = input("How old are you?")
now = datetime.datetime.now()
diff = 100 - int(age)
print('Hi '+name+" you will be 100 years old in ",(now.year+diff))