#1 ask a num with user and filter and add into the old list :
#2 ask a num with the user and filter even and add into the even list :
#3 ask a age with user and check he/she is eligible for vote(must be greater than 19) or not
#Application of loop into the weeks of day :
# for example :
        #Day 1 is --> Sunday
        #Day 2 is --> Monday
#5Ask a first_name and second_name from user and return its full name as :
    # for example : oh! So, your full name is : John Doe
    

#1 

odd_list = []
even_list = []
def filter_odd_even(user_provided_num) :
 for num in range(1,user_provided_num+1):
         [even_list.append(num) if num %2 ==0 else odd_list.append(num)]
number = int(input("Please provide the number : "))        
filter_odd_even (number)
print(f"The odd numbers are : {odd_list} ")



#2

odd_list = []
even_list = []
def filter_odd_even (user_provided_num) :
    for (num) in range (1,user_provided_num+1) :
        [even_list.append(num) if num %2 == 0 else odd_list.append(num)] 
numbers = int(input("Please provide the number : "))
filter_odd_even(numbers)
print(f"The even numbers are : {even_list}")



#3
age = int(input(" Please provide your age : "))
if age >=19 : 
    print("You are eligible for the vote.")
else : 
        print("You are not eligible for the vote.")
        
        
        
#4
week_days_list = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"]
counter = 0
for day in week_days_list:
    counter += 1
    print(f"The day {counter} is :--> {day} ")
        
        

#5
first = input("Please enter your first name : ")
last = input("Please enter your last name : ")
def full_name(first,last):
        return f"{first}{last}"
print(f"Oh! So, Your full name is {first} {last}")
