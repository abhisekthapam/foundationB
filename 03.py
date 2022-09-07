name, age, place, email = input("What is your name?  What is your age?  Where do you live?  What is your email address? ").split()
intage = int(age)
if intage >=100:
    print("You are too old. Just go to sleep.")
if intage <=12:
    print("You are too young. You can code but First focus in your study.")
elif intage >12 :
  print(f"My name is {name}. Iam {age} years old. I live in {place}. My email is {email}.")
 