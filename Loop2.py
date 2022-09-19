odd_list = []
even_list = []
def filter_odd_even(user_provided_num):
    for num in range(1,user_provided_num+1):
      [even_list.append(num) if num %2 ==0 else odd_list.append(num)]
#something if condition else something       
any_num = int(input("Please provide any number :-->:"))
filter_odd_even(any_num)
print(f"Now, the odd list is : {odd_list}")
print(f"Now, the even list is : {even_list}")

