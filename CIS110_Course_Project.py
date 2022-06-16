import time, os, sys
def typingPrint (text):
    for character in text: 
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.09)


import time, os, sys
def typingInput (text):
    for character in text: 
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.09)

typingPrint("Hey there! I have a fun interactive story to share with you! ")
typingPrint("First, I need to ask a few questions. ")
typingPrint("This story is going to be based on you and a few of your favorite things. ")
typingPrint("Don't forget, to submit your reply, simply press 'enter.' Let's get started! ")

typingPrint("\n")

input("Press 'enter' to continue ")

typingPrint("\n")

userName= input ('What is your name?  ')
while(len(userName) == 0):
    userName = input("Please enter your name: ")

typingPrint("\n")

if userName.lower() == "brianna": 
   typingPrint(userName + "? I love that name! ")
else:
   typingPrint("Hello, " + userName + " Nice to meet you!")

typingPrint("\n")

dogName=input ("Chose a name for the yorkie:  ")
while(len(dogName) == 0):
    dogName = input("Enter a name: ")

typingPrint("\n")

majorCity=input ("What is your favorite major city?  ")
while(len(majorCity) == 0):
    majorCity = input("Enter a city name: ")

typingPrint("\n")

resturantName= input ("What is the name of your favorite resturant? ")
while(len(resturantName) == 0):
    resturantName = input ("Enter a resturant name: ")

typingPrint("\n")

favoriteDessert=input ("What is your favorite dessert?  ")
while(len(favoriteDessert) == 0):
    favoriteDessert = input ("Enter a dessert: ")

typingPrint("\n")

favoriteNumber=input ("What is your favorite number?  ")
while(len(favoriteNumber) ==0):
    favoriteNumber = input("Enter your favorite number: ")


typingPrint("\n")

typingPrint("This is gonna be fun! Let's get started! ")

typingPrint("This is a story about a yorkie named " + dogName +". ")

typingPrint("\n")

typingPrint(dogName + " was left alone for a night while her owner, " +  userName +" went out.")
typingPrint("Today was " + dogName + "'s opportunity to have a night out herself. So, she decided to roam the streets of " + majorCity)
typingPrint("to find this new pet spa she heard about. ")
typingPrint(dogName + " waited a while after her owner had left, then she ran out of the doggy door and out into the busy streets.")

typingPrint("\n")

typingPrint("While walking down the sidewalk, " + dogName + " arrived at " + resturantName + " . And she couldn't help noticing all the ")
typingPrint(favoriteDessert + "s being made. 'Yummmmm', She thought as she ran to the window and starred. ")

sneakIntoResturant = input("Should " + str(dogName) + " sneak into the resturant ? Type yes or no: ")

if sneakIntoResturant == "yes":
   typingPrint(dogName + " ran through the resturant and straight to the ktchen, she had to have a " + favoriteDessert + "!")
   typingPrint("One of the servers noticed " + dogName + " and put some of the delicous dessert on a plate for the dog to enjoy.")
   typingPrint(dogName+ " loved it so much, she ate " + favoriteNumber + "!")
   typingPrint("Unfortunately, some of the customers caught sight of the dog enjoying her dessert in the kitchen and it upset them, causing some of them to leave")
   typingPrint("One of the customers even called Animal Rescue to come pick the dog up and take her home. But they were too late. When they got to the returant, the dog was long gone. ")
else: 
   typingPrint("The yorkie decided not to go into the resturant because she did not want to get her fur  all dirty.")

typingPrint("\n")

typingPrint("After the resturant,"+ dogName + " finally makes it to the pet spa.")
typingPrint("It was just as she pictures it! A cute little place with dogs like her relaxing and getting pampered!")
typingPrint(dogName +" was so excited to get here, she forgot to decide what service she even wanted done. A massage? A pawicure?")

NailService= input("Should she get a pawicure or a massage? Type P or M:")

if NailService == 'P':
   typingPrint("\n)
   typingPrint("Eventually, She decides on a pawicure and gets a glossy coat of pink nail polish on her paws. The yorkie was having so much fun, she forgot she had to be home by 10:00pm!")
   typingPrint("After spending a day in " + majorCity +", " + dogName + " decided she could'nt run home before " + userName + " got back, because ")
   typingPrint("she would mess up her nails.")
   typingPrint("Luckily, when " + userName + " got home and found the yorkie missing, they knew exactly where to find her. ")
   typingPrint("The silly dog did'nt realize her owner was going to suprise her with a trip to the spa the next day.")
else: 
    typingPrint("The yorkie decides to get a massage. All of this running through the city has made her tense")
    typingPrint("The massage was so relaxing, she fell asleep "+ dogName + ". She had to run home before her owner got back.")
    typingPrint("Lucky for her, she got home just in time")

print("------------ The End--------------")
