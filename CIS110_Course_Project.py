tyingPrint("Hey there! I have a super cute fun and interactive story to share with you! ")
tyingPrint("First, I need to ask a few questions. ")
tyingPrint("This story is going to be based on you and a few of your favorite things. ")
tyingPrint("Don't forget, to submit your reply, simply press 'enter.' Let's get started! ")

tyingPrint("\n")

input("Press 'enter' to continue ")

tyingPrint("\n")

userName= input ('What is your name?  ')
while(len(userName) == 0):
    userName = input("Please enter your name: ")

tyingPrint("\n")

if userName.lower() == "brianna": 
   print(userName + "? I love that name! ")
else:
   print("Hello, " + userName + " Nice to meet you!")

tyingPrint("\n")

dogName=input ("Chose a name for the yorkie:  ")
while(len(dogName) == 0):
    dogName = input("Enter a name: ")

tyingPrint("\n")

majorCity=input ("What is your favorite major city?  ")
while(len(majorCity) == 0):
    majorCity = input("Enter a city name: ")

tyingPrint("\n")

resturantName= input ("What is the name of your favorite resturant? ")
while(len(resturantName) == 0):
    resturantName = input ("Enter a resturant name: ")

tyingPrint("\n")

favoriteDessert=input ("What is your favorite dessert?  ")
while(len(favoriteDessert) == 0):
    favoriteDessert = input ("Enter a dessert: ")

tyingPrint("\n")

favoriteNumber=input ("What is your favorite number?  ")
while(len(favoriteNumber) ==0):
    favoriteNumber = input("Enter your favorite number: ")


tyingPrint("\n")

tyingPrint("This is gonna be fun! Let's get started! ")

tyingPrint("This is a story about a yorkie named " + dogName +". ")

tyingPrint("\n")

tyingPrint(dogName + " was left alone for a night while her owner, " +  userName +" went out.")
tyingPrint("Today was " + dogName + "'s opportunity to have a night out herself. So, she decided to roam the streets of " + majorCity)
tyingPrint("to find this new pet spa she heard about. ")
tyingPrint(dogName + " waited a while after her owner had left, then she ran out of the doggy door and out into the busy streets.")

tyingPrint("\n")

tyingPrint("While walking down the sidewalk, " + dogName + " arrived at " + resturantName + " . And she couldn't help noticing all the ")
tyingPrint(favoriteDessert + "s being made. 'Yummmmm', She thought as she ran to the window and starred. ")

sneakIntoResturant = input("Should " + str(dogName) + " sneak into the resturant ? Type yes or no: ")

if sneakIntoResturant == "yes":
   tyingPrint(dogName + " ran through the resturant and straight to the ktchen, she had to have a " + favoriteDessert + "!")
   tyingPrint("One of the servers noticed " + dogName + " and put some of the delicous dessert on a plate for the dog to enjoy.")
   tyingPrint(dogName+ " loved it so much, she ate " + favoriteNumber + "!")
   tyingPrint("Unfortunately, some of the customers caught sight of the dog enjoying her dessert in the kitchen and it upset them, causing some of them to leave")
   tyingPrint("One of the customers even called Animal Rescue to come pick the dog up and take her home. But they were too late. When they got to the returant, the dog was long gone. ")
else: 
   tyingPrint("The yorkie decided not to go into the resturant because she did not want to get her fur  all dirty.")

tyingPrint("\n")

tyingPrint("After the resturant,"+ dogName + " finally makes it to the pet spa.")
tyingPrint("It was just as she pictures it! A cute little place with dogs like her relaxing and getting pampered!")
tyingPrint(dogName +" was so excited to get here, she forgot to decide what service she even wanted done. A massage? A pawicure?")

NailService= input("Should she get a pawicure or a massage? Type P or M:")

if NailService == 'P':
   tyingPrint("Eventually, She decides on a pawicure and gets a glossy coat of pink nail polish on her paws. The yorkie was having so much fun, she forgot she had to be home by 10:00pm!")
   tyingPrint("After spending a day in " + majorCity +", " + dogName + " decided she could'nt run home before " + userName + " got back, because ")
   tyingPrint("she would mess up her nails.")
   tyingPrint("Luckily, when " + userName + " got home and found the yorkie missing, they knew exactly where to find her. ")
   tyingPrint("The silly dog did'nt realize her owner was going to suprise her with a trip to the spa the next day.")
else: 
    tyingPrint("The yorkie decides to get a massage. All of this running through the city has made her tense")
    tyingPrint("The massage was so relaxing, she fell asleep "+ dogName + ". She had to run home before her owner got back.")
    tyingPrint("Lucky for her, she got home just in time")

print("------------ The End--------------")
