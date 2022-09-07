
name = input("What is your name? ")
age = input("How old are you? ")
place = input("Where do you live? ")
contact_number = input("What is your phone numer? ")
email = input("What is your email? ")
print(f'''My name is {name}. 
Iam {age} years old. 
I live in {place}. 
My phone number is {contact_number}. 
My email address is {email}''')
while  True :
 song = input(' Would you like to listen music? '' (yes/no) ')
 if song == "no":
      print("Sorry but You must listen. It's not you who will decide hahaha...")
 elif song == "yes":
      music = input ("Which song would you like to listen? ")
      print("Sorry we have only 1 song right now and you must listen to that hahaha...")
      print("Song is playing...")
      from playsound import playsound
      playsound("C:\\Users\\DELL\\Videos\\Anime Theme Songs\\Dreaming ON OnePiece.mp3")
 else:
   print("Please...Type (yes/no) only")
   
      
      
      