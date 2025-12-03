#................................TASK 1...................................................................
# 11. Assign values "Orange", "Banana", "Cherry" to multiple variables x, y and z in one line respectively.
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# 12. Assign the values 10, "John", and True to the variables age, name, and is_student in a 
# single line.
age, name, is_student = 10, "John", True
print(age)
print(name)
print(is_student)
# 13. Swap the values of x and y, where x = 5 and y = 10, without using a temporary variable.
x = 5
y = 10
x, y = y, x
print(x)
print(y)
# 14.	Create a list of numbers with values 1, 2, and 3. Unpack the list into separate 
# variables a, b, and c.
a, b, c = (1, 2, 3)
print("a", a)
print("b", b)
print("c", c)
# 15. Convert a string variable called height from “1.35” to a float.
height = "1.35"
height_float = float(height)
print(type(height_float))
# 16.	Predict the output of the following statements:
# a) bool("")  # False
# b) bool(123)  # True
# c) bool(["apple", "cherry", "banana"])  # True
# d) bool(False)  # False
# e) bool(None)  # False
# f) bool(0)  # False
# g) bool("abc")  # True
# h) bool(())  # False
# i) bool([])  # False
# j) bool({})  # False


#...................................TASK 2..........................................
# 1. Write a program that asks the user for their name and then greets them with their 
# name: Print a greeting message that includes the user's name in the format "Hello, {name}!".
# name = input("What is your name?: ")
# print(f"Hello, {name}")
# 2. Ask the user for their birth year and calculate their age. Print the user's age in the 
# format “You are {age} years old.”.
# birth_year = input("What year were you born?: ")
# from datetime import datetime
# age = datetime.now().year - int(birth_year)
# print(f"you are {age} years old")
# 3. Ask the user for their favourite color. Print a statement that includes the color in the format “Your favorite color is {favourite_color}.”.
# favorite_color = input("What is your favourite colour?: ")
# print(f"Your favourite colour is {favorite_color}")
# 4. Ask the user to input some text and check if it is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. `madam` or `nurses run` or `121`.
# Print a statement in the format “It is {is_palindrome} that {text} is a palindrome.”. `is_palindrome` is either `True` or `False`.
text = input("Write some palindrome texts here: ")
is_palindrome = text == text[::-1]
print(f"It is {is_palindrome} that the {text} is a palindrome")

# 5. Create a program that asks the user to input a password and checks if it meets certain criteria (at least 8 characters and not more than 30 characters).
# Print a statement in the format “It is {is_valid} that the password fulfils the criteria.”. `is_valid` is either `True` or `False`.
# Bonus point if you can hide the password input from displaying on the screen as clear text.
from getpass import getpass
password = getpass("Enter password: ")
password_min_length = 8
password_max_length = 30
is_valid = (password_min_length <= int(password) <= password_max_length)
print(f"It is {is_valid} that the password fulfils the criteria.")
# 6. Write a program that asks the user for their weight (in kilograms) and height (in meters) and calculates their Body Mass Index (BMI). Calculate the BMI using the formula BMI = weight / (height ** 2). Round the BMI to 2 decimal places. Print a statement in the format “Your BMI is {BMI}”.
# weight = input("What is your weight in kg?: ")
# height = input("What is your height in meters?: ")
# BMI = round(int(weight)/(float(height) ** 2), 2)
# print(f"Your BMI is {BMI} kg/m square")