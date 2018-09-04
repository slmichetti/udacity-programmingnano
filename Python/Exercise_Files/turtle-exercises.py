import turtle
t=turtle.Turtle()
fav_color="purple"

sides=[1,2,3,4,5]
go=100
turn=72
t.color(fav_color)
for side in sides:
    t.forward(go)
    t.right(turn)

import turtle
mary = turtle.Turtle()
fav_color = "purple"
sides=[1,2,3,4,5]
go=100
turn=72
mary.color("fav_color")
for side in sides:
    mary.forward(go)
    mary.right(turn)


color = "purple"
sides = [1, 2, 3, 4, 5]
angle = 72
distance = 100
mary.color(color)
for side in sides:
    mary.forward(distance)
    mary.right(angle)

 import turtle
juno = turtle.Turtle()
juno.color("white")
for side in [1,2,3]:
    juno.forward(100)
    juno.left(120)

import turtle
amy = turtle.Turtle()
amy.color("cyan")
some_list=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for item in some_list:
    amy.forward(50)
    amy.right(30)

import turtle

lengths = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

dizzy = turtle.Turtle()
dizzy.color("blue")
dizzy.width(5)

for length in lengths:
    dizzy.forward(length)
    dizzy.right(90)

 same result:
 for side in [10, 20, 30, 40, 50, 60]:
    dizzy.forward(side)
    dizzy.right(90)

 same result:
 for angle in [10, 20, 30, 40, 50, 60]:
    dizzy.forward(angle)
    dizzy.right(90)



  import turtle

links = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sides = [1, 2, 3, 4, 5, 6]
angles = [20, 20, 20]
weaver = turtle.Turtle()
weaver.width(5)
weaver.speed(10)
weaver.color('orange')

# Move back so the chain is centered.
# weaver.penup()
# weaver.back(80)
# weaver.pendown()

for link in links:
    # Draw a hexagon.
    for side in sides:
        weaver.forward(40)
        weaver.right(60)

    # Scoot over to the next link.
    weaver.penup()
    weaver.forward(50)
    weaver.left(35)
    weaver.pendown()

weaver.hideturtle()


import turtle
anna = turtle.Turtle()
for path in [1, 2, 3, 4]:
    for step in [1, 2, 3]:
        anna.forward(10)

The turtle goes forward 10 pixels each time anna.forward(10) is called, and this happens 12 times total, because 4 × 3 = 12. 
So it goes 120 pixels forward in total.


import turtle
amy = turtle.Turtle()
# Make the width thicker so that the line will be easier to see
amy.width(5)
# Move back without drawing anything
amy.penup()
amy.back(140)
amy.pendown()

# Draw three lines of different colors, with space in between
for prettycolor in ["red", "orange", "yellow"]:
    amy.color(prettycolor)
    amy.forward(50)
    amy.penup()
    amy.forward(50)
    amy.pendown()


 # Draw three shapes of different colors, with space in between
for prettycolor in ["red", "orange", "yellow"]:
  amy.color(prettycolor)
  for side in [1, 2, 3, 4]:
        amy.forward(50)
        amy.right(90)
  amy.penup()
  amy.forward(100)
  amy.pendown()

When Python runs the line of code print(shake(move(23))), the first thing it does is run the move function, with the input 23. 
The result of move(23) is then passed to the shake function, and the result of that is passed to print.

The input function always returns a string.

def parrot():
    x = input()
    print(x)

parrot()
parrot()
parrot()

Will read three lines of input from the user's keyboard, printing out each orange

 A for loop needs a list, range, or other iterable value. 
 It won't work with an integer or a turtle; and an import statement is not a value at all.

 def too_long(s):
    return len(s) > 140

  ALSO WORKS
  def too_long(word):
    if len(word) > 140:
        return True
    else:
        return False

def start_K(w):
	if word[0] == K:
		return True
	else:
		return False

MY Abracadabra


Abracadabra: Solution
Here's one way to write the word_triangle function in the exercise above:

def word_triangle(word):
  length = len(word)
  for n in range(length):
    print(word[:length - n])
The slice expression here is word[:length - n]. Since length stays the same while n grows, this means that on each pass through
the loop, length - n gets smaller and smaller, from length down to 1. And that means that on each pass, the string that gets 
printed will be a shorter and shorter piece of word.


def middle(a, b, c):
    if b >= a >= c or c >= a >= b:
       return a
    if a >= b >= c or c >= b >= a:
       return b
    if a >= c >= b or b >= c >= a:
       return c

   def total_of_three():
   	one = input("Enter a number: ")
   	two = input("Enter another number: ")
   	three = input("Enter a third number: ")
   	result = int(one) + int(two) + int(three)
   	print(f"{one} + {two} + {three} = {result}")


def starts_with(long, short):
	#get the length of the short word to set up how many letters get compared
	length = len(short) 
	#use that value to set up the comparison with the long word
	beginning = long[0:length] #number from length into the splice tells it how many to compare
	return beginning == short #sets up true false without an if statement b/c if they aren't equal, it will return False
#can simplify by doing this
	def starts_with(long, short):
		return long[0:len(short)] == short 

Option 2
def starts_with(long, short):
	#uses for loop
	for posiition in range(len(short)): #the lenght of the word sets up how many times the loop will run
	  if long[position] != short[position]:
	  	return False
	return True
    #this method evaluates position by position until it proves out to be true or false

Option 3
#can simplify #1
	def starts_with(long, short):
		return long[0:len(short)] == short 



String predicates
Python comes with a lot of features already built in. Although you can write the starts_with function yourself, it's actually already available as a method on strings —

>>> "banana".startswith("ban")
True
>>> "bonobo".startswith("ban")
False

another is endswith 
Can use predicates in if statements

def possible_tag(word):
    if word.startswith("<") and word.endswith(">"):
        print(word, "could maybe be an HTML tag")
    else:
        print(word, "is definitely not an HTML tag (but might contain one)")


def good_length(word):
	if len(word) < 8:
		print("2short")
	if len(word) >= 8 and len(word) <= 64:
		print("nice password, yo")
	if len(word) > 64:
		print("This is really much too long for a password. I mean its really secure, but I dont want to type this much every time I log in , okay?")
        
good_length('123dfidkjler45')



The secret of booleans
There is a third boolean operation called not:

not x is true if x is false.
not x is false if x is true.
An interesting consequence of these rules is that not (x and y) is the same as (not x) or (not y). Similarly, not (x or y) is the same as (not x) and (not y).


In Python, you can also use other values as if they were booleans. For instance, you can use a string, number, or list as the condition in an if statement. Python will treat it as if it's a True or False value, according to these rules:

For numbers, zero values are considered false, and all nonzero values are considered true.
For strings, the empty string is considered false, and all nonempty strings are considered true.
For lists, the empty list is considered false, and all nonempty lists are considered true.
This can be a little bit tricky. For example:

if [False]:
    print("It's true!")
else:
    print("No, it's false!")
This code will print It's true! because the condition [False] is a nonempty list. Even though it contains the value False, it's still a true value.

Python programmers sometimes call this automatic conversion "truthiness". 

A list can contain any number of items. A list with zero items is the empty list: []
A list can contain items of any type. For instance, [1, 2, 3] is a list of integers; ["red", "orange"] is a list of strings.
You can use a list with a for loop. The code inside the for loop will run once for each item in the list. On each pass, the loop variable will take on the next value from the list. For example:
for x in [7, 8, 9]:
    y = x + 1
    print(f"After {x} comes {y}.")
This loop will print the following output:

After 7 comes 8.
After 8 comes 9.
After 9 comes 10.

In Python, lists and strings have some things in common. They are both sequence types — they represent a collection of values, not just a single value. 
The items inside a string are characters; the items inside a list can be anything.

Three operations you've seen on strings actually work on all sequence types: the indexing operation, the slicing operation, and the len function. Since they work on all sequences, they work on lists, too:

>>> words = ["The", "Queen", "rules", "wisely."]
>>> words[1]
'Queen'
>>> words[1:3]
['Queen', 'rules']
>>> len(words)
4

Just as the length of a string is the number of characters in it, 
the length of a list is the number of items in it.

total_length - takes a list of strings and returns the sum of the lengths of all the strings in that list

def total_length(strings):
	total = 0
	for s in strings:
		total = total + len(s)
	return total

def total_length(strings):
	return sum(map(len, strings))

MINE:
def total_length(strings):
	return len(''.join(strings)) + len([string])


The append method adds items to the end of a list. Doesnt return a value - but modifies the list.

The extend method does something quite different from append.  
	Extend modifies a list by copying another list and adding them at the end. It treats a string as if it 
	   is an individual list of characters
When you pass a list to words.extend, it adds the items from that list to words.

The reverse method reverses the order of a list.
	reverse turns a list from back to front

The sort method modifies a list so that it is in sorted order.
	words list is put into alphabetical order

All of these methods have some things in common - all work on a list and all modify that list but dont return any value

MUTABILITY and SHARED STRUCTURE
 - You cant modify a string like you can a some_list
 mutable = changeable (immutable = unchangeable)
 strings are immutable; lists are mutable meaning they can be changed while a program is running


Suppose you have these variables:

noun = "wolf"
verbs = ["runs", "eats", "boogies"]
Which one of the following statements is an error because strings are immutable? 
 ou can't modify the values inside of a string in Python, so noun[0] = "g" is an error. The other statements are not errors.

x += 1 (read: x plus equals 1)
The effect of x = x + 1 and x += 1 is exactly the same.
The latter is called an augmented assignment statement, because it's an assignment statement but it augments the existing value rather than replacing it.


dog = "woof"
dog *= 2
'woofwoof'
The * operation on strings is used to repeat a string. You can't multiply a string by a string, but you can "multiply" a string by an integer, to repeat a string some number of times.

Doing this does not break the rule that strings are immutable, because it isn't altering the contents of the string — it's replacing the value of the variable.

If you have a variable called toobig and you want it to divide its value by two, how could you do that using an augmented assignment? 
toobig/= 2

LOOPING OVER strings

for x in "many words":
    print(x)
It prints out each character of many words on its own line
When you treat a string as a sequence, the items in that sequence are the single characters of the string.

for x in ['many', 'words']:
...   print(x)
... 
many
words

COUNTING IN A String
One thing you can do with loops is to count things. A for loop over a string is a natural choice to do things like count letters in that string.

Count the x's
Write a function count_x that takes a string as input and returns the number of times the letter "x" occurs in that string.

This counts all items in the string:
def count_x(string):
	total = 0
	for x in string:
  		total += 1
  	return total

Count the x's:  DOESNT WORK......
def count_x(string, target):
	total = 0
	for x in string:
		if x == target:
			total += 1
		return total 

Count any character, solution
Here's one solution to the exercise on counting characters:

def count_ch(string, target):
    total = 0
    for ch in string:
        if ch == target:
            total += 1
    return total


 For - repeat section of code for each item in range, list or other iterable
 While loop repeats a section of code as long as some condition is true
   while has a condition - will run until a condition is true 

 it uses a boolean expression or condition to decide if it should run the code inside of it, but 
   unlike an if statement - it can run that code many times (an if will only run it once)

def count_ch(string, target):
    index = 0
    total = 0
    while index < len(string):
        if string[index] == target:
            total += 1
        index += 1
    return total


def until_dot (s):
	index = 0
	while index < len(s) and s[index] != '.':
		#this says while the index length is less then the string and the index refers to a position in the string
		#says index is less than the length of the string and the character at that posiiton is not a .
		index += 1
		#inside the loop - increases the value of the index variable by 1 and moves until it encounters a . or at the end of the length of the string
	return s[:index]
	  	#the value of the index will be either the length of the string or the locatino of the first dot, so if you take
	  	#a slice from the beginning of the string, up to the index, that will be the portion of the string up to the first dot, which is what you wanted to return

def until_dot(s): #using a for loop
  for index in range(len(s)):
  	  #if statement that looks to see if hte character at that location in the string is a dot. If it is, we return the slice up to the dot
  	  if s[index] == '.':
  	  	  #a dot! return eveverything up to here
  	  	  return s[:index]
  	  #we ran out of stirng without seeing any dots
  return s


Both of these are examples of a technique called linear search. In a linear search, we start at the beginning of a sequence and look at each item 
in the sequence until we find one that matches what we're looking for. When we either find it, or run out of items, we stop.


INFINITE LOOPING
expression true is a constant expression; repeats the code while the condition is true. in these, the condition
is always true, so it always runs. Condition on while statement is always true, it will never existing

Ctrl-C to exit the loop

Another way to exit from an infinite loop. Inside a while or for loop you can use the break statement to immediately exit the loop -

def no_repeating():
	words = []
	while True:
		word = input("Tell me a word: ")
		if word in words:
			print("You told me that word already!")
			break
		words.append(word)
	return words

When python runs the break statement, it skips down to the line after the end of the while loop.

A break statement will always skip to the end of the innermost while or for loop. If you have a loop inside another loop,
it will only exit the inside loop.

Locating a substring
Earlier in this lesson, you learned the indexing syntax, using an integer inside[ square brackets ] to access individual characters of a string:

>>> word = "cookbook"
>>> print word[4]
b

When we search a string for substrings, we'll use index numbers to describe where the substring is found. For instance, if we search for 'ook' in 'cookbook', we'll say that it's found at positions 1 and 5. This means that if we take a slice of length 3 starting from one of these positions, we'll see that substring:

>>> location = 5
>>> size = 3
>>> word[location : location+size]
ook


def starts_with(long, short):
#determine if a string starts with a given substring. takes two string arguments, long and short and returns a boolean value
  for position in range(len(short)):
  	if long[position] != short[position]:
  		return False
  	return True

 def starts_with_v2(long, short):
 	length = len(short)
 	beginning = long[0 : length]
 	if beginning == short:
 		return True
 	else:
 		return False

 def starts_with_v3(long, short):
 	return long[0:len(short)] == short 


>>> import re
>>> if re.search("ABCD" , "xxxxABCDyyyy"):
...  print "found"
...
found


def is_substring(x, y)
  index = 0
  y.find(x) != -1


THEIR Solution

def is_substring(short, long):
	index = 0
	while index < (len(long) - len(short) + 1):
		if long[index : index + len(short)] == short:
			return True
		index += 1
	return False

In is_substring, we use this expression:

long[index : index + len(short)] == short
The difference between these is that index is added to both sides of the slice expression. 
Where the former uses 0, the latter uses index; and where the former uses len(short), the latter uses index + len(short).


#count substrings, not just characters (ex use this function to count the number of <p> tags in an HTML doc)
count_substring can have overlapping matches

def count_substring(string, sub):
    count = start = 0
    while True:
    	start = string.find(sub, start) + 1
    	if start > 0:
    		count+=1
    	else:
    		return count

	while index < (len(long) - len(short) + 1):
		if long[index : index + len(short)] == short: 
			return True
		index += 1
	return False

def count_substring_v2(string, sub)
	ln = len(sub)
	print(sum(sub == s[i:i+ln] for i in xrange(len(s)-(ln-1))))

	for i in range(len(string)-2):
		if string[i:i+3] == sub:
			total += 1
	print('Number of times substring occures is: ', total)


ANOTHER ONE - count count_occurences
def count(sequence, item):
cont=0
for i in sequence:
    if item==i:
        cont+=1
return cont

THIS ONE WORKS

def count_occurences(string, sub):
    count=0
    for i in range(0, len(string)-len(sub)+1):
        if sub in string[i:i+len(sub)]:
            count=count+1
    print 'Number of times sub occurs in string (including overlaps): ', count


THEIRS
count_substring, solutions
Here are two different versions of the count_substring function.

def count_substring_v1(string, target):
    count = 0
    index = 0
    while index < len(string) - len(target) + 1:
        if string[index : index + len(target)] == target:
            count += 1
        index += 1    # <- look here
    return count

def count_substring_v2(string, target):
    count = 0
    index = 0
    while index < len(string) - len(target) + 1:
        if string[index : index + len(target)] == target:
            count += 1
            index += len(target)   # <- look here
        else:
            index += 1
    return count

 That's right! The count_substring_v1 function sees three instances of 'AA' in the string 'AAAA', 
 whereas the count_substring_v2 function sees only two, since it does not count the one in the middle.


def locate_first(string, sub):
	index = 0
	while index < (len(string) - len(sub) + 1):
		if string[index : index + len(sub)] == sub:
			return index
		index += 1
	return -1 #not return False

def locate_all(sub, string):
  i = 0
  try:
  	while True:
  		i = string.index(sub, i)
  		yield i 
  		i += 1
  except ValueError:
  	pass


 def locate_all(string, target):
    matches = 0 #
    index = 0
    while index < len(string) - len(target) + 1:
        if string[index : index + len(target)] == target:
            matches.append(index) #missed this
            index += len(target)   
        else:
            index += 1
    return matches


indexing - for extracting a single character
slicing - for extracdting a group of characters
JOIN- method on strings that is useful for building a single string out of a list of strings

" ".join(words)
"silly".join(words)
'my silly dog silly has silly fleas'

Also works with a variable

attributeerror - means lists do not have a method called join; its only on strings
string you want to use as the joiner always goes first

string.join(list) inside the parentheses of the method call


def breakify(strings):
	#putting <br> tags between strings
	return "<br>".join(strings)


truth = "beauty"
index = 0
letters = []
while index < len(truth):
    letters.append(truth[index])
    index += 2

letters = '-'.join(letters)
print(letters)
b-a-t
The loop advances the index variable by 2 on each pass, so it skips every other letter in the original word 'beauty'. Then the join method puts a hyphen in between the letters.


