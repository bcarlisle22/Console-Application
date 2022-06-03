print("Hey there! I have a super cute fun and interactibe story to share with you!")
print("First, I need to ask a few questions. ")
print("This story is going to be based on you and a few of your favorite things")
print("Don't forget, to submit your reply, simply press 'enter.' Let's get started! ")


input("Press 'enter' to continue ")

userName= input ('What is your name?  ')
if userName.lower() == "brianna": 
   print(userName + "? That name sounds familar! ")
else:
   print("\n Hello, " + userName + " Nice to meet you!")

print("\n")
dogName=input (" \n Chose a name for the yorkie:  ")
majorCity=input ("\n What is your favorite major city?  ")
resturantName= input ("\n What is the name of your favorite resturant?  ")
favoriteDessert=input ("\n What is your favorite dessert?  ")
favoriteNumber=input ("\n What is your favorite number?  ")




print("\n")

print("Woohoo, this is gonna be fun! Let's get started! ")

print("This is a story about a yorkie named " + dogName +". ")

print("\n")

print(dogName + " was left alone for a night while her owner, " +  userName +" went out.")
print("Today was " + dogName + "'s opportunity to have a night out herself. So, she decided to roam the streets of " + majorCity)
print("to find this new pet spa she heard about. ")
print(dogName + " waited a while after her owner had left, then she ran out of the doggy door and out into the busy streets.")

print("\n")

print("While walking down the sidewalk, " + dogName + " arrived at " + resturantName + " . And she couldn't help noticing all the ")
print(favoriteDessert + "s being made. 'Yummmmm', She thought as she ran to the window and starred. ")

sneakIntoResturant = input("Should " + str(dogName) + " sneak into the resturant ? Type yes or no: ")

if sneakIntoResturant == "yes":
   print(dogName + " ran through the resturant and straight to the ktchen, she had to have a " + favoriteDessert + "!")
   print("One of the servers noticed " + dogName + " and put some of the delicous dessert on a plate for the dog to enjoy.")
   print(dogName+ " loved it so much, she ate " + favoriteNumber + "!")
   print("Unfortunately, some of the customers caught sight of the dog enjoying her dessert in the kitchen and it upset them, causing some of them to leave")
   print("One of the customers even called Animal Rescue to come pick the dog up and take her home. But they were too late. When they got to the returant, the dog was long gone. ")
else: 
   print("The yorkie decided not to go into the resturant because she did not want to get her fur  all dirty.")

print("\n")

print("After the resturant,"+ dogName + " finally makes it to the pet spa.")
print("It was just as she pictures it! A cute little place with dogs like her relaxing and getting pampered!")
print(dogName +" was so excited to get here, she forgot to decide what service she even wanted done. A massage? A pawicure?")

NailService= input("Should she get a pawicure or a massage? Type P or M:")

if NailService == 'P':
   print("Eventually, She decides on a pawicure and gets a glossy coat of pink nail polish on her paws. The yorkie was having so much fun, she forgot she had to be home by 10:00pm!")
   print("After spending a day in " + majorCity +", " + dogName + " decided she could'nt run home before " + userName + " got back, because ")
   print("she would mess up her nails.")
   print("Luckily, when " + userName + " got home and found the yorkie missing, they knew exactly where to find her. ")
   print("The silly dog did'nt realize her owner was going to suprise her with a trip to the spa the next day.")
else: 
    print("The yorkie decides to get a massage. All of this running through the city has made her tense")
    print("The massage was so relaxing, she fell asleep "+ dogName + ". She had to run home before her owner got back.")
    print("Lucky for her, she got home just in time")

print("------------ The End--------------")



