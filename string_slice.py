"""Write a program that will take as input, a string and two integers. The two integers will represent indices. If the string can be sliced using the two indices then print the sliced string. 
If either or both of the integers are outside the strings index range then print that the string cannot be sliced at those integers."""

string = input("Enter a string to be sliced.\n")
slice1 = int(input("Enter the first index to be sliced.\n"))
slice2 = int(input("Enter the second index to be sliced.\n"))


if len(string) < int(slice1) or len(string) < int(slice2):
    print("Cannot slice string using those indices.")

#result = string [slice (slice1, slice2)]
#print (result)

#prints cannot slice string, but then prints the slice remaining after slice1

#solution:
else:
    print(string[slice1:slice2])