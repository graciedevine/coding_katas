
print('How many cats do you have?')
numCats= input()
try:
    if int (numCats) >=4:
        print ("That's a lot of cats!")

    elif int (numCats) <0:
        print ("Please enter a value greater than 0")
        
    elif int (numCats) >0 and int(numCats) < 4:
        print("That’s a reasonable number of cats.")
while True:
    except ValueError:
            print ('Please enter a numeric value.')
break