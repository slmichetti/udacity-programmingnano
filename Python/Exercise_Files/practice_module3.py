#extract a piece of a filename
def extract_place(filename):
	first = filename.find("_")
	partial = filename [first + 1:]
	second = partial.find("_")
	return partial[:second]


#Tutorial Solution:
#filename.split("_") - using the split function
#split operation - splits a string into a list of strings, using 
#filename split using "_" and extract pos[1] to return the portion of the string
def extract_place(filename):
	return filename.split("_")[1]

#creating directories for the places that have been identified in filename
def make_place_directories(places):
		for place in places:
			os.mkdir(place)
#if you ask os to make a directory that already exists, it will 
#stop with an error
#can modfiy the make place fx so tht it never tries to create duplicate dirs or 
#make sure there are no duplicates being passed from the list

#Move a file from Photos directory to the Florida directory
import os
filename = "Flamingos.png"
os.rename(os.path.join("Photos", filename),
          os.path.join("Florida", filename))

#Print characters from a file, each on a separate line
f = open("words.txt")  
for a in f:
   for b in a:
      print(b)
#In each pass through the outer loop, the loop variable a gets assigned a line of the file. 
#In each pass through the inner loop, the variable b gets assigned a character of the line a

#Rude Words detector
rude_words = ["crap", "darn", "heck", "jerk", "idiot", "butt", "devil"]

with open("filename.txt") as filename:
	contents = filename.read()
	words = contents.split(" ")
	rude_count = 0
	for word in words:
		if word in rude_words += 1
		print (f"Found rude word: {rude}")
if rude_count == 0:
	print("Your file has no rude words")
	print("At least no rude words I know")
#write a loop that gets one line at a time instead of consuming the whole file
#do this with feature of open

#More Efficient Rude Words detector
#Rude Words detector v2

import string

rude_words = ["crap", "darn", "heck", "jerk", "idiot", "butt", "devil"]

def check_line(line):
	rude_count = 0
	words = line.split(" ")
	for word in words:
		word = word.string(string.punctuation)
		if word in rude_words:
			rude_count += 1
			print (f"Found rude word: {word}")
	return rude_count

def check_file(filename):
	with open(filename) as filename:
		rude_count = 0
		for line in filename:
			rude_count += check_line(line)

	if rude count == 0
		print("Message no rude words")


if __name__ == '__main__':
	check_file("filename")



Practice
#create new file in write mode
#f = open("new_file.txt", "w")

#use loop to write all the even numbers from 0 to 30 to your new file
with open("new_file.txt", "w") as writer:
	#write even numbers 0 to 30
	for num in range (0, 31):
		if num % 2 == 0:
			#f.write(str(num)) -- should be
			writer.wrte(f"{num}\n")
			#f.write("\n")

#copy contents of read.txt to another file
with open("read.txt") as f:
	with open("out.txt") as f1:
		#for line in f:
		#	f1.write(line)
		f1.write(f.read())
f1.close()
f.close()


#solution from stackoverflow
with open("read.txt") as f:
	with open("out.txt", "w") as f1:
		for line in f:
			f1.write(line)


#class and subclass creation practice
class Dog:
	scientific_name = "Canis lupus familiaris"

	def __init__ (self, name):
		self.name = name
		self.woofs = 0  #keeps track of how high the dog is supposed to count

	def speak(self):
		print("Woof!")

	def eat(self, food):
	    if food == "food":
	      print("Yummy food!")
	    else:
	      print("That's not really food.")
	
	def learn_name(self, name):
		self.name = name 
	
	def hear(self, words):
	    if self.name in words:
	    	self.speak()

	def count(self)		
		self.woofs += 1
		for bark in range(self.woofs):
			self.speak()

class Pitbull(Dog):
	origin = "England"

	def speak(self):
		print("WOOF!")

class Cat:
	origin = "Wonderland"

	def speak(self):
		print(random.chocie(["Meow Meow!", "Purr!"]))

#using super for the init when creating a subclass
class BigBlueTurtle(turtle.Turtle):
   def __init__(self):
     super().__init__()
     self.color("blue")
     self.width(10)