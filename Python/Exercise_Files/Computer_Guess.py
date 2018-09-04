----------------------------------------------------------------------
Other practice code
----------------------------------------------------------------------
def computer_guess(num):
...   low = 1
...   high = 1000
...   guess = 500
...   while guess != num:
...     guess = (low+high)//2
...     print("The computer takes a guess..", guess)
...     if guess > num:
...       high = guess
...     elif guess < num:
...       low = guess + 1
...   print("The computer guesses", guess, "and it was correct!")
#this works but I want the computer to ask me for the number

def computer_guess(num):
	print("Pick a number from 1 to 1000.")
	print("I will make a guess.")
	print("If I am right, type 'c")
	print("If the number is higher than my guess, type 'h'")
	print("If it's lower, type 'l'")
	low = 1
	high = 1000
	guess = 500
	while guess != num:
		guess = (low+high)//2
		print("The computer takes a guess..", guess)
		ans=input(write)
		if ans not in ("y", "i", "h"):
			print("Huh?")
			continue
		if ans =="y":
			print("I guessed it! Your number is", guess)
		elif ans == "h":
			low == guess + 1
		elif ans == "l":
			high == guess - 1 

def computer_guess(num):
	print("Pick a number from 1 to 1000.")
	print("I will make a guess.")
	print("If I am right, type 'c")
	print("If the number is higher than my guess, type 'h'")
	print("If it's lower, type 'l'")
	low = 1
	high = 1000
	guess = 500
	while guess != num:
		guess = (low+high)//2
		print("The computer takes a guess..", guess)
		ans = input ("Enter h, l or c.")
		if ans =="c":
			print("I guessed it! Your number is", guess)
		elif ans == "h":
			low == guess + 1
		elif ans == "l":
			high == guess - 1

			


	print("Please think of a number between 1 and 1000")
	low = 1
	high = 1000
	guess = 500
	while guess != num:
		guess = (low+high)//2
		print("Is your secret number..", guess, "?")
		ans = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate my guess is correct.")
		if ans == 'h':
			high == guess
		elif ans == 'l':
			low == guess	
		elif ans == 'c':
			print ("Game over. Your secret number was:", guess)
			break
		else:
			print("Sorry, I did not understand your input")



#Computer attempts to guess a number you choose between 1 and 1000 in 10 tries
#user chooses number in given range
high = 1000
low = 1

def getnum():
	#get a number from the user
	x = ""
	while not x or x > high or x < low:
		print("Enter a number between %s and %s" % (1, 100))
		x = input()
		try:
			x = int(x)
		except ValueError:
			x = getno()
		return(x)

def halfway(low, high):
	#find integer approx halfway point between two values.
	x = (low+high)//2

def computer_guess():
	#computer finds number by halving
	no1 = low
	no2 = high
	usernum = getnum()
	compguess = ""
	count =  #no of guesses it took the computer to get the number

	while compguess != usernum:
		count += 1
		compguess = halfway(no1, no2)
		print('%s. I guess %s' % (count, compguess))
		if compguess > usernum:
			no2 = compguess
		elif compguess < usernum:
			no1 = compguess
		elif compguess == usernum:
			print("Got it!")
		else:
			print("I'm a loser. I didn't get it")




THEIR answer



print("Think of a number between 1 and 1000. I am going to try to guess it in 10 tries.")
low = 1
high = 1000
guess = 500
number = 0
while number not in range (1, 1001):
	number = int(input("\nChoose your number: "))

while guess != num:
	attempts = 10
	guess = (low+high)//2
	while attempts != 0:
		print("I guess: ", guess)
		print("Type 'l' if my guess is too low")
		print("Type 'h' if my guess is too high")
		print("Type 'c' if I guess your number correctly.")
		humanans = input("So did I guess right?")
		if humanans == "h":
			low == guess + 1
			attempts = attempts - 1
			print(attempts, "attempts left")
			guess = ((low+high)/2)
		elif humanans == "l":
			high == guess - 1
			attempts = attempts - 1
			print(attempts, "attempts left")
			guess = ((low+high)/2)
		elif humanans == "c":
			print("Woo hoo. I won! Your number is: ", guess)
	else:
		answer = input ("Do you want to play again? (yes/no)")
else:
	print("Thank you for playing. Goodbye")

