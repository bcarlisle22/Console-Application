import time, os, sys
def typingPrint (text):
    for character in text: 
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)


import time, os, sys
def typingInput (text):
    for character in text: 
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)

        
keepGoing="y"
while keepGoing.lower()== "y":

typingPrint("Hey there! I have a fun interactive story to share with you! ")
typingPrint("First, I need to ask a few questions. ")

print("\n")

typingPrint("This story is going to be based on you and a few of your favorite things. ")
typingPrint("Don't forget, to submit your reply, simply press 'enter'. ")

print("\n")


typingPrint("Let's get started!")

print("\n")


input("Press 'enter' to continue ")

print("\n")


userName= input ('What is your name?  ')
while(len(userName) == 0):
    userName = input("Whoops. I don't think I got that. Please enter your name: ")

print("\n")

if userName.lower() == "brianna": 
   typingPrint(userName + "? I love that name! ")
else:
   typingPrint("Hello, " + userName + " . Nice to meet you!")

print("\n")

dogName=input ("Chose a name for the yorkie:  ")
while(len(dogName) == 0):
    dogName = input("Whoops. I don't think I got that. Enter a name: ")

print("\n")

majorCity=input ("What is your favorite major city?  ")
while(len(majorCity) == 0):
    majorCity = input("Whoops. I don't think I got that. Enter a city name: ")

print("\n")

resturantName= input ("What is the name of your favorite resturant? ")
while(len(resturantName) == 0):
    resturantName = input ("Whoops. I don't think I got that. Enter a resturant name: ")

print("\n")

favoriteDessert=input ("What is your favorite dessert?  ")
while(len(favoriteDessert) == 0):
    favoriteDessert = input ("Whoops. I don't think I got that. Enter a dessert: ")

print("\n")

favoriteNumber=input ("What is your favorite number?  ")
while not favoriteNumber.isdigit():
    favoriteNumber = input("Whoops. I don't think I got that. Enter your favorite number: ")


print("\n")

typingPrint("Let's start the story! ")

print("\n")
print("------------------------------------------------------------")
print("\n")
print("\n")

typingPrint("This is a story about a yorkie named " + dogName +". ")

print("\n")

typingPrint(dogName + " was left alone for a night while her owner, " +  userName + ", went out.")
print("\n")
typingPrint("Tonight was " + dogName + "'s opportunity to have a night out herself. So, she decided to roam the streets of " + majorCity)
typingPrint(" to visit a new pet spa she heard about. ")
typingPrint(dogName + " waited a while after her owner had left, then she ran out of the doggy door and out into the busy streets.")

print("\n")

typingPrint("While walking down the sidewalk, " + dogName + " arrived at " + resturantName + " . And she couldn't help noticing all the ")
typingPrint(favoriteDessert + "s being made.'Yummmmm', She thought as she ran to the window and starred. ")

print("\n")

sneakIntoResturant = input("Should " + str(dogName) + " sneak into the resturant ? Type 'yes' or 'no': ")
while sneakIntoResturant.lower() != "yes" and sneakIntoResturant.lower() != "no":
    sneakIntoResturant = input("Whoops. I don't think I got that. Please type 'yes' or 'no': ")
    
if sneakIntoResturant == "yes":
    
   print("\n")
   typingPrint(dogName + " ran through the resturant and straight to the kitchen, she had to have a " + favoriteDessert + " !")
   typingPrint("One of the servers noticed " + dogName + " and put some of the delicous dessert on a plate for the dog to enjoy.")
   typingPrint(dogName+ " loved it so much, she ate " + favoriteNumber + " of them! ")
   typingPrint("Unfortunately, some of the customers caught sight of the dog enjoying her dessert in the kitchen and it upset them, causing some of them to leave. ")
   typingPrint("One of the customers even called Animal Rescue to come pick the dog up and take her home. But they were too late. When they got to the returant, the dog was long gone. ")
else: 
   print("\n")
   typingPrint("The yorkie decided not to go into the resturant because she did not want to get her fur all dirty.")

print("\n")

typingPrint("After the resturant,"+ dogName + " finally makes it to the pet spa. ")
typingPrint("It was just as she pictured it! A cute little place with dogs like her relaxing and getting pampered! ")
typingPrint(dogName +" was so excited to get here, she forgot to decide what service she even wanted done. A massage? A pawicure?")

print("\n")

nailService= input("Should she get a pawicure or a massage? Type 'p' or 'm': ")
while nailService.lower() != "p" and nailService.lower() != "m":
    nailService = input("Whoops. I don't think I got that. Please type 'p' or 'm': ")

if nailService.lower() == 'p':
    
   print("\n")
               
   typingPrint("Eventually, she decides on a pawicure and gets a glossy coat of pink nail polish on her paws. ")
   typingPrint("\nThe yorkie was having so much fun, she forgot she had to be home by 10:00! ")
else: 
    typingPrint("The yorkie decides to get a massage. All of this running through the city has made her tense.")
    typingPrint(" The massage was so relaxing, " + dogName + " fell asleep. She woke up in a jolt and ran home as fast as could. ")
    typingPrint("She had to hurry run home before her owner got back.")

  print("\n")

Method = input("Should the yorkie run home or stay at the salon? Type 'r' or 's': ")
while Method.lower() != "r" and Method.lower() != "S":
    Method = input("Whoops. I don't think I got that. Please type 'r' or 's': ")

    
if nailService.lower() == 'p' and  Method.lower() == 's':
   
   print("\n")
   
   typingPrint("It was 9:58 and " + dogName + " didn't think she would make it home before " + userName + " got back. ")
   typingPrint("Besides, she would mess up her nails. So she waited and waited hoping her owner would come get her. " )
   print("\n")
   typingPrint("Luckily, when " + userName + " got home and found the yorkie missing, " + userName+ " knew exactly where to find her. ")
   typingPrint("When " + userName + " got to the salon, they picked " + dogName + " up and said ")
   typingPrint("'You know it's not safe to roam the streets by yourself.")
   typingPrint("..and you didnt need to.' ")
   typingPrint("\n")
   typingPrint(dogName + " was confused")
   print("\n")
   typingPrint(userName+ " explained it to her on the way home. ")
   typingPrint("The silly dog didn't need to sneak out to the spa because her owner was going to suprise her with a trip to the spa the next day.")
elif nailService == "p" and Method == "r":
    typingPrint(dogName + " decided to try to run home anyways. She was a block away from her home when Animal Rescue spotted her and started chasing her. ")
    typingPrint("She ran into her front yard just as " + userName + " pulled into the driveway.")
    typingPrint(userName + " spotted Animal rescue chancing " + dogName + " . ")
    typingPrint("'Hey! This is my dog! '" + userName + " said. Animal Rescue apologized and promptly left. ")
    typingPrint("The dog and her owner went inside the house.")
    typingPrint("That's the first and last time " + dogName + " is going to leave the house without her owner. ")
else: 
   print("\n")
   typingPrint(dogName+ " ran home as fast as she could before her owner got back. ")
   typingPrint("Lucky for her, she got home just in time! ")
   print("\n")
   typingPrint(dogName + " was already snugged up in bed when " + userName + " opened the front door. ")
   typingPrint("'That was close', " + dogName + " thought. As her owner came closer to greet her. ")
   typingPrint( userName + " looked at her and said, 'Hmmmm, someone smells like......nail polish.' ")
   print("\n")
   typingPrint("BUSTED!")
   
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")

print("------------------------ The End-----------------------------")

print("\n")
print("\n")
print("\n")
print("\n")
print("\n")

keepGoing=input( "Do you want to play again? Please enter y or n : ")
else:
    typingPrint("See you next time!")
    


      
    
    
