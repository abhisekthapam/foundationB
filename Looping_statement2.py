#2 Ask an information of your Laptop and a function should return like this :
"""
Brand_Name MOdel_Name available_at price

    """

Laptop = input("Which laptop do you want to buy? ")
if Laptop == "dell":
 print('''Your laptop brand name is Dell
Your Model number is Dell G15 5520
Available price is 1,85,000. ''')
else :
    print("We have only dell brand laptop right now.")
