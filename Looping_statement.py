#1 Ask a two integer number with the user and a function should return their adition.

first_number = int(input("Please enter the number : "))
last_name = int(input("Please enter the second number : "))
#creation of addition function
def addition(x,y):
 sum = x+y
 return sum 
#calling addition function
print(f"The sum return by the function is : {addition(first_number, last_name)}")
