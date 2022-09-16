#2 Ask an information of your Laptop and a function should return like this :

from unicodedata import name

brand = input("Please enter the brand name : ")
model = input("Please enter the model number : ")
price = input("Please enter the price : ")
def laptop_info(brand,model,price):
 return f"{brand} {model} @Rs.{price}"

print(f"Your laptop is : {laptop_info(brand,model,price)}")
