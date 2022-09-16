#Loops in python
#Range function in python
#print(f"The range from 1 to 10 is : {range(1,10+1)}")

#List objects
num_list = []

week_days_list = ["Sunday"
"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"]

for num in range(1,11):
    print(f"The number in range is : --> {num}")
    num_list.append(num)  
    
print(num_list)

counter = 0
for day in week_days_list :
    counter += 1
    print(f"The {counter} day is : -->{day}")
    
#Same progress with the help of range function 
for position in range(0,len(week_days_list)):
 print(f"The {position} position in day is : -->{week_days_list[position]}")
 
#
for position in range(0,len(week_days_list)):
 print(f"The {position+1} ####### day is : -->{day}")
 
 
odd_list = []
even_list = []
def filter_odd_even(user_provided_num):
    for num in range(1,user_provided_num+1):
        if num % 2 ==0:
         even_list.append(num)
        else:
         odd_list.append(num)
any_num = int(input("Please provide any number :-->:"))
filter_odd_even(any_num)
print(f"Now, the odd list is : {odd_list}")
print(f"Now, the even list is : {even_list}")