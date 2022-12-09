#program to guess a number
import random
def nameask():
   name = input("what is your name? :")
   print("Hello " + name + " in this game you will guess a number between 1 and 5\n")
   return name

def numchoice():
   a = random.randint(1, 5)
   c = int(input("please choose a number between 1 and 5.\n"))
   if c == a:
      print("correct!")
   else:
      print("incorrect! Answer was: " + str(a))
   return 0

def keepplaying():
   num=1
   while(num == 1):
      numchoice()
      int(input("would you like to play again(1 for yes, any key for no)"))

nameask()
keepplaying()
