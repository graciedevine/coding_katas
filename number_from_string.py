"""Write a program that takes a string from the user and prints the first number encountered along with it's position. You can assume the number is a single digit"""

#Input string
#Iterate over string
#Find number in string
#Print number and index

s = input("Enter a string:\n")

i = 0
while i <len(s) and not s[i].isdigit():
    i += 1

if i <len(s):
    print(s[i], (i))
else:
    print("No digits were found in string.")




