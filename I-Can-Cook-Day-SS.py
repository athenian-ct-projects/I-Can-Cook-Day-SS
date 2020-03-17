#final project - build your own cupcake (these are a couple options, but you don't need to follow through)!!!!!!!
#flavors - chocolate, vanilla, strawberry
#filling - strawberries, chocolate, nuts, none
#frosting - chocolate, buttercream, cream cheese
#sprinkles - rainbow, chocolate, white, none
#drinks - water, lemonade, coffee

print("Hello! You are playing the dessert game!") 
print ("This includes a series of questions about your preferences about a cupcake.") 
print ("Then, you'll get your final product - a virtual dessert")


name = input("what is your name")
print ("hello " + name)

def printMakingcupcakes():
  print("let's get making")

printMakingcupcakes()

print ("Now, we will start with cupcake flavors")
flavor = input ("What is your favorite flavor")
print ("your favorite flavor is " + flavor)

print ("Now, we will choose your favorite cupcake filling")
filling = input ("What is your favorite filling, if you would like no filling, type 3")
x = filling
if x == '3':
  print ('you have no filling')
elif x != '3':
  print ("your favorite filling is " + filling)

print ("Now, we will choose your favorite cupcake frosting")
frosting = input ("What is your favorite frosting")
print ("your favorite frosting is " + frosting)

print ("Now, we will choose your favorite type of sprinkles")
sprinkles = input ("What are your favorite kind of sprinkles")
print ("your favorite kind of sprinkles are " + sprinkles)

numberofsprinkles = int(input ("How many sprinkles would you like? "))
for x in range (numberofsprinkles):
  print ("I added sprinkles")

print ("Last step, choose a random drink with your cupcake")

numberofdrinks = int(input ("enter a number from 0-2, corresponding to a drink:"))

listofdrinks = ["water", "lemonade", "coffee"]
print(listofdrinks[numberofdrinks])
#im pouring the drink
print("Let me know when to stop")
pour = ""
while pour != "stop":
  pour = input ('Im gonna pour your drink - type "stop" to stop') 
print ("You have your drink!")

printMakingcupcakes()

print ("You've made a cupcake with "+ flavor + " and " + filling + " and " + frosting + " and you have " + sprinkles + " and " + (listofdrinks[numberofdrinks]))
