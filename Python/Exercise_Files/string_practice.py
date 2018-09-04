#find the length of a word, print, then for every loop through, remove one letter and print that word minus the letter
def word_triangle(word):
	length=len(word)
	for n in range(length)
		print(word[:lenth - n])

#Function to take a string as input and return that string with "ly" appended to it
def adverbly(s)
  return(s + 'ly')

#function that takes three string arguments and returns the one that is between the others in string sort order
def middle_string(a, b, c):
	if a <=b <= c or a <=c <= b:
		return 'a'
	elif b <=a <= c or b <= c <= a:
		return 'b'
	elif c <=a <= b or c <=b <= a:
		return 'c'

#function that uses input to ask the user for three numbers, then prints the sum of those numbers
def total_of_three():
  num1 = input("Enter a number:")
  num2 = input("Enter another number:")
  num3 = input("Enter a third number:")
  result = int(num1) + int(num2) + int(num3)  
  print (f"{num1} + {num2} + {num3} = {result}") 

#function that takes two strings as arguments, and determines if the first string starts with the second string
def starts_with(word, w):
	for position in range(len(short)):
		if word[position] != short[position]:
			return False
		else:
			return True

#function that takes a string and returns True if the string is between 8 and 64 characters long
def good_length(word):
	length=len(word)
	if length in range(8, 64):
		return True #print("Great job. Your password is a good length")
	else:
		return False #print("Sorry, your password is not strong enough")

#function that takes a list of strings and returns the sum of lengths of all the strings in that list
def total_length(strings):
	total = 0
	for s in strings:
		total = total + len(s)
	return total

def total_length_v2(strings):
	return sum(map(len, strings))


#function that takes a string as input and returns the number of times the letter "x" occurs in that string
def count_x(s):
	print(s.count("x")) #returns number of times x appears in the string

#function that takes a string and a character and returns the number of times that character appears in that string
def count_ch(text, target):
	result = 0
	for ch in text:
		if ch == target:
		  result += 1
	return result


def count_ch_v2(string, target):
    index = 0
    total = 0
    while index < len(string):
        if string[index] == target:
            total += 1
        index += 1
    return total
	
#function that takes a string argument and returns the portion of that string before the first dot character. if no dots, return full string
def until_dot(s):
	index = 0
	while index < len(s) and s[index] != '.':
		return s[:index]

#alternative provided by instructor
def until_dot_v2(s):
	for index in range(len(s)):
		if s[index] == '.':
			retrn s[:index]
		return s

#abracadabra word triangle
def word_triangle(word):
  length = len(word)
  for n in range(length):
    print(word[:length - n])





 
