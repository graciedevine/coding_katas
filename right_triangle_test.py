print("Enter three known sides of your triangle to determine if it's a right triangle.")
input_a = int(input("Please enter the first value."))
input_b = int(input("Please enter the second value."))
input_c = int(input("Please enter the third value."))

a = input_a
b = input_b
c = input_c

if a**2 + b**2 == c**2:
   print("This forms a right triangle.")
else:
   print("Sorry, this isn't a right triangle.")

   
