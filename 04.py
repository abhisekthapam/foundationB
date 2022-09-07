name, age, place = input("What is your name?, How old are you?, Where do you live?: ").split()
intage = int(age)
if intage <=16 :
    print("You are too young for this program.") 
elif intage > 16 :
    print(f"My name is {name}. Iam {age} years old. I live in {place}.")
    