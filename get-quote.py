#importing random for generating random numbers
import random

def Primary():
#opening files
  f = open("quotes.txt")
#storing lines
  quotes = f.readlines()
#now close the file
  f.close()

#last is storing postition of last quote
  last = len(quotes) - 1
#using randint to pick random line 
  rnd = random.randint(0,last)
  print(quotes[rnd])
#python entrypoint
if __name__== "__main__":
#calling function
  Primary()
