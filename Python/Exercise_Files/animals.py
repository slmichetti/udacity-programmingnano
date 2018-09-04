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

	def count(self):	
		self.woofs += 1
		for bark in range(self.woofs):
			self.speak()

class Cat:
	
	def speak(self):
		print(random.chocie(["Meow Meow!", "Purr!"]))

class Pitbull(Dog):
	origin = "England"

	def speak(self):
		print("WOOF!")