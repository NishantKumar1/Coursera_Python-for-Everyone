# Converting user Input
# if we want to read a number from the user
# we must convert it from a string to a anumber using a type conversion function.
# Later we will deal with bad input data
# Convert elevator floors
inp = input("Europe floor?")
usf = int(inp) + 1
print("Us floor", usf)

print("123"+ "abc")

_spam = 42
print(_spam)

spam_23 = 42
print(spam_23)

spam_23 = 42
print(spam_23)

SPAM_23 = 43
print(SPAM_23)

42%10
print(42%10)

x = int(98.6)
print(x)

# Write a program to prompt the user for hours and teater per hours using input
# to compute gross pay. use 35 hours and a rate of 2.75 per hours to tet the program.
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about the error checking a bad user data.

# This is the fisrt line is provided to you.

hours = input("Please enter hours :")
rate = input("Please enter your rate card details : ")
pay = float(hours) * float(rate)
print("Your gross pay is : ", pay)