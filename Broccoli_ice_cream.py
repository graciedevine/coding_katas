
#Say hello
print ('Hootie-toot.')

#Ask if someone likes broccoli

myAnswer= input ('Do you like broccoli?')

if myAnswer.lower () == 'yes':
	print ('Mmmmmm, yummy')

while myAnswer.lower() == 'no':
	print ("BUT IT'S GOOD FOR YOU!")
	break

#Ask if someone likes ice cream

while myAnswer.lower()== 'yes':
	myAnswer=input ('Do you like ice cream?')
	break

if myAnswer.lower( )== 'yes':
	print ('ME TOO!')

while myAnswer.lower() == 'no':
	print ("WHAT'S WRONG WITH YOU?")
	break

#Ask if someone likes broccoli ice cream

while myAnswer.lower()== 'yes':
	myAnswer=input ('Do you like broccoli ice cream?')
	break
if myAnswer.lower () == 'yes':
	print ('You nasty.')

while myAnswer.lower() == 'no':
	print ("Congratulations, you have passed!")
	break




