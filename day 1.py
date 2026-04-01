# Print command
print(" Hello Nishant")

print("Welcome to AI Journey")

# Variable (Core Learning)
name = "Nishant"
age = 21
goal = "AI Engineer"

print("My name is", name)
print("My age is", age)
print("My goal is to become an", goal)

# Play with Code
# Change values:
# Try diferent name
# Try different age
# Add:

name = " Mamata"
age = 43
goal = "Housewife"

print("My name is", name)
print("My age is", age)
print("My goal is to become a", goal)

# Add
city = " Delhi"
print("I live in", city)

# Print what is Variable?
# variable is like a container that holds data.
name = "Nishant" # Stores text
age = 21 # Stores number

# Data Types
# 1- String(str)--- Text data
name = "Nishant"
# 2- Integer(int)--- Whole numbers
age = 21
# 3- Float(float)--- Decimal numbers
height = 5.9
# 4- Boolean(bool)--- True or False
is_student = True
# 5- List(list)--- Collection of items
fruits = ["apple", "banana", "cherry"]
# 6- Dictionary(dict)--- Key-value pairs
person = {"name": "Nishant", "age": 21, "goal": "AI Engineer"}
# 7- Tuple(tuple)--- Immutable collection of items
coordinates = (10, 20)
# 8- Set(set)--- Unordered collection of unique items
unique_numbers = {1, 2, 3, 4, 5}
# Example
lst_1 = ["apple,", "banana", "cherry"]
type(lst_1)
print(type(lst_1))

tuple_1 = ("apple", "banana", "cherry")
type(tuple_1)
print(type(tuple_1))

# Create Variables
nmae = "Nishnat"
age = 42
height = 5.9
is_student = True

print(name)
print(age)
print(height)
print(is_student)

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

print("My name is", name)
print("My age is", age)
print("My height is", height)
print("Am I a student?", is_student)

# Type checking
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


# Practice (Critical)
city = "Delhi"
dream_job = " President of world top company in AI & Machine Learning"
study_hours = 5

print("I live in",city)
print("My dream job is to become", dream_job)
print("I study for", study_hours,"hours daily")

# Challenge

a = 10
b = 20
print(a+b)
print(a*b)

# this is the first comment
spam = 1 # and this is the second comment
text = "# This is not a comment becuase it's inside quotes"

# Numbers
2 +2

50-5*6

(50-5*6)/4

8/5

# Claissic division return a float
17/3

# Floor division discards the fractional part

17//3

# the modulo operator returns the remainder of the division
17%3

# floored quiotient * divisor + remainder 
 5 *3 +2

#5 Squared
5**2

# 2 to the power of 7

2**7

# use \' to escape the sigle quote
'doesn\'t'

# use ... or use double quotes to avoid escaping single quote
"doesn't"

s = " First line.\nSecond line." # \n means newline
s # without print() it will show the \n as part of the string
'Fist line .\n Second Line.'
print(s)

print('c:\this\name') # \t means tab and \n means newline

print(r'c:\this\name') # r before the string means raw string and it will ignore the escape characters
# Strings can be concatenated (glued together) with the + operator, and repeated with * operator.
# 3 times 'un' + 'ium'
3 * 'un' + 'ium'

# Two or more strings literals(i.e the ones encloased between quotes) next to each other are automatically concatenated.
'py' 'thon'

# This feature is particularlry user when you want to break long strings.

text = ('Put seval strings within parentheses '
        'to have them joined together.')
text

# Strings can be indexed (subscripted), with the first character having index 0. There is no separate character type; a single character is simply a string of length 1.
word = 'python'
word[0] # Character in position 0
word[5] # Character in position 5

# Indices may also be neagative numbers, to start counting from the right
word[-1] # Last characte
word[-2] # Second last character
word[-6] # First character

# Note that since -0 is the same as 0, negative indices must start from -1.
# In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters, slicing allows you to obtain substring of a string by specifying a range of indices.
word [0:2]# Characters from position 0 (included) to 2 (excluded)
word[2:5] # Characters from position 2 (included) to 5 (excluded)

# Slice indices have user defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced. So, in this case, word[:2] returns the first two characters of the string, and word[4:] returns the last two characters.

word[:2]
word[0:2]
word[2:5]

# Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.
word[:2]
word[4:]
word[-2 :]

# Note how the start is always included and the end is always excluded. This makes sure that s[:i] + s[i:] is always equal to s.
word[:2]
word[2:]
word[:2] + word[2:]

word[:4]
word[4:]
word[:4] + word[4:]

word[42]# the word has only 6 characters
word[4:42]
print(len(word))
print(word)

'j' + word[1:]

s = 'supercalifragilisticexpialidocious'
print(len(s))

# Lists
# Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type.
# List are ordered, can store anything, is mutable(changeable) and is defined by square brackets [].
squares = [1,2,3,4,5]
print(squares)
print(len(squares))

squares[0] # indexing returns the item
squares[-1] # index from the end of the list

# lists also support operations like concatenation
lst = squares + [6,7,8,9,10]
print(lst)

# list also suppport cubes
cubes = [1,8,27,64,125]
print(len(cubes))
cubes[0]
cubes[-1]
cubes[-1:]
cubes[-3:]
cubes[-5:]
cubes[-5:-2]

#list.append() method adds a single item to the end of the list. The item can be of any type: a number, a string, another list, and so on.
cubes.append(216)
print(len(cubes))
print(cubes)

rgb = ['red', 'green', 'blue']
rgb.append("yellow")
print(rgb)
rgba = rgb
print(rgba)
id(rgb)== id(rgba)
rgb.append("white")
print(rgb)

correct_rgb = rgb[:]
correct_rgb[-1] = "pink"
print(correct_rgb)

letters = ["a","b","c","d","e"]
letters.append("g")
print(len(letters))

# replace some values
letters[2:5] = ["C","D","E"]
print(letters)

# remove some values
letters[2:5] = []
print(letters)
print(len(letters))

# clear the list by replacing all the elements with an empty list
letters [:] = []
print(letters)
print(len(letters))

# len function returns the number of items in a list
print(len(squares))

# nest list is a list that contains other lists as its elements. For example, the following list contains three sublists:
a = ["a","b","c"]
n = [1,2,3]
x = [a,n]
x[0]
x[0][1]
x [0][0]
x[0][2]


