# Exercise 1
# An amusement park ride has these rules:
# - Must be at least 120 cm tall to ride.
# - If under 120 cm but with an adult, still allowed.
# - Otherwise, not allowed.

# height = int(input("Enter height: "))
# with_adult = input("With adult? ").lower()  
# print("\n\nExercise 1")
# if height >= 120:
#     print("Allowed")
# elif height < 120 and with_adult == "yes":
#     print("Allowed")
# else:
#     print("Not allowed")

# Example input/output executions:
# Enter height: 130
# With adult? no
# Output: Allowed
#
# Enter height: 110
# With adult? yes
# Output: Allowed
#
# Enter height: 110
# With adult? no
# Output: Not allowed

# Enter height: 119
# With adult? yes
# Output: Allowed
#
# Enter height: 100
# With adult? no
# Output: Not allowed
#
# Enter height: 150
# With adult? no
# Output: Allowed
# 

# Exercise 2
# An exam grading system with retake rule:
# The user enters exam score and retake status ("yes" or "no").
# - If score is at least 50, print "Pass".
# - If score is less than 50 but retake is "yes", print "Retake allowed".
# - If score is less than 50 and no retake, print "Fail".


# exam_score = int(input("Enter your exam score here: "))
# retake_status = input("Are you retaking the course?: ").lower()
# if exam_score >=50:
#   print("Pass")
# elif exam_score < 50 and retake_status == "yes":
#   print("Retake allowed")
# elif exam_score < 50 and retake_status == "no":
#   print("Fail")

# student_score = int(input("Enter your score here: "))
# retake = input("will you retake the course: ").lower()
# print("\n\nExercise 2")
# if student_score >= 50:
#   if retake == "yes" or retake == "no":
#     print("Pass")
# elif student_score < 50:
#   if retake == "yes":
#     print("Retake allowed")
#   else:
#     print("Fail")
# Example input/output executions:
#
# Enter score: 42
# Retake? yes
# Output: Retake allowed
#
# Enter score: 42
# Retake? no
# Output: Fail
#
# Enter score: 50
# Retake? no
# Output: Pass
#
# Enter score: 75
# Retake? yes
# Output: Pass
#
# Enter score: 10
# Retake? no
# Output: Fail

# Exercise 3
# A ride-hailing app calculates trip approval:
# The user enters distance (km) and wallet balance.
# Each km costs 200 units.
# - If wallet balance is enough for the trip, print "Trip confirmed".
# - If balance is less but at least half the cost, print "Add funds".
# - If less than half, print "Trip denied".

# distance = int(input("Enter distance covered in km: "))
# wallet_balance = int(input("Enter your wallet balance: "))
# tfare = distance * 200
# print("\n\nExercise 3")
# if wallet_balance >= tfare:
#    print("Trip confirmed")
# elif wallet_balance >= tfare / 2:
#    print("Add fund")
# else:
#    print("Trip denied")

# Example input/output executions:
#
# Enter distance: 10
# Enter wallet balance: 800
# Output: Trip denied
# Reasoning: cost = 10 * 200 = 2000; half = 1000; balance = 800.
# 800 < 1000 (less than half), so "Trip denied".
#
# Enter distance: 10
# Enter wallet balance: 2000
# Output: Trip confirmed
# Reasoning: cost = 2000; balance = 2000.
# balance >= cost, so "Trip confirmed".
#
# Enter distance: 10
# Enter wallet balance: 1000
# Output: Add funds
# Reasoning: cost = 2000; half = 1000; balance = 1000.
# not enough (1000 < 2000) but balance >= half, so "Add funds".
#
# Enter distance: 10
# Enter wallet balance: 400
# Output: Trip denied
# Reasoning: cost = 2000; half = 1000; balance = 400.
# balance < half, so "Trip denied".
#
# Enter distance: 5
# Enter wallet balance: 500
# Output: Add funds
# Reasoning: cost = 5 * 200 = 1000; half = 500; balance = 500.
# not enough (500 < 1000) but exactly half, so "Add funds".



# Exercise 4
# An airport boarding system:
# The user enters boarding pass ("yes"/"no") and passport ("yes"/"no").
# - If both are "yes", print "Proceed to boarding".
# - If boarding pass is missing, print "No boarding pass".
# - If passport is missing, print "No passport".
# - If both missing, print "Denied entry".
# boarding_pass = input("Do you have a boarding pass?: ").lower()
# passport = input("Do you have a passport?: ").lower()
# print("\n\nExercise 4")
# if boarding_pass == "yes" and passport =="yes":
#   print("Proceed to boarding")
# elif boarding_pass == "no" and passport =="no":
#   print("Denied entry")
# # elif boarding_pass == "no":
# #   print("No boarding pass")
# # elif passport =="no":
# #   print("No passport")

# # Example input/output executions:
# #
# # Boarding pass? no
# # Passport? yes
# # Output: No boarding pass
# #
# # Boarding pass? yes
# # Passport? no
# # Output: No passport
# #
# # Boarding pass? no
# # Passport? no
# # Output: Denied entry
# #
# # Boarding pass? yes
# # Passport? yes
# # Output: Proceed to boarding
# #
# # Boarding pass? no
# # Passport? yes
# # Output: No boarding pass




# # ..................................SECOND ASSIGNMENT.............................................
# print("\n\n                        SECOND ASSIGNMENT")
# # Collect two numbers as input from the user and assign as variables, a and b, write an if 
# # statement that prints "a and b are both positive" if both a and b are positive, prints 
# # "Only one is positive" if one of them is positive, and prints "Neither is positive" if 
# # # neither is positive.
# # a = int(input("Enter any number: "))
# # b = int(input("Enter another number: "))
# # print("\n\nQuestion 1")
# # if a > 0 and b > 0:
# #   print("a and b are both positive")
# # elif a > 0 or b > 0:
# #   print("Only one is positive")
# # else:
# #   print("Neither is positive")


# # Collect three numbers x, y and z as a comma separated string input from the user and print "Increasing order" if they are in STRICTLY increasing order, "Decreasing order" if they are in STRICTLY decreasing order, and "Neither" otherwise.
# numbers = input("Enter three numbers separated by commas: ")
# print("\n\nQuestion 2")
# x, y, z = numbers.split(",")
# if x < y < z:
#   print("Increasing order")
# elif x > y > z:
#   print("Decreasing order")
# else:
#   print("Neither")


# # Write a program that reads a string called `palindrome` supplied through user input and checks if it is a palindrome. Print "Is a palindrome" if it is, otherwise print "Not a palindrome".
# palindrome = input("Enter a word: ")
# palindrome_entered = palindrome.replace(" ", "").lower()
# print("\n\nQuestion 3")
# if palindrome_entered == palindrome_entered[::-1]:
#   print("Is a palindrome")
# else:
#   print("Not a palindrome")


# # You have three variables: x, y, and z collected as 3 separate inputs from the user. Write an if statement that checks if exactly two out of the three variables are equal and prints "Two are equal" if this is true. Otherwise, print "All different" or "All same" accordingly.
# x = input("Enter a number: ")
# y = input("Enter another number: ")
# z = input("Enter the last number: ")
# print("\n\nQuestion 4")
# if (x == y and x != z) or (x == z and x != y) or (y == z and y != x):
#     print("Two are equal")
# elif x == y == z:
#     print("All same")
# else:
#     print("All different")
  
# Given three angles angle1, angle2, and angle3 collected as 3 separate inputs from the user, use if statements to check if they can form a valid triangle. Print "Valid triangle" if the sum of the angles is 180 degrees and all angles are greater than 0. Otherwise, print "Invalid triangle".

# angle1 = int(input("Enter an angle in degree: "))
# angle2 = int(input("Enter another angle in degree: "))
# angle3 = int(input("Enter a new angle in degree: "))
# print("\n\nQuestion 5")
# if angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3 == 180):
#     print("Valid triangle")
# else:
#     print("Invalid triangle")

# You have a single character variable `ch` supplied through user input. Write an if statement that prints "Vowel" if ch is a vowel (a, e, i, o, u, both uppercase and lowercase), and "Consonant" otherwise. Assume that the input is a single alphabet character.
# character = input("Enter a variable: ").lower()
# vowel = ("a, e, i, o, u")
# print("\n\nQuestion 6")
# if character  in vowel:
#   print("vowel")
# else:
#   print("consonant")

# Given a comma separated string input from the user of three colors color1, color2, and color3, write an if statement to check if all three colors are primary colors (red, blue, yellow). Print "All primary colors" if they are, otherwise print "Not all primary colors".
# colors = input("Enter 3 primary colors seperated by comma: ").lower()
# color1, color2, color3 = colors.strip().split(", ")
# primary_colors = {"red", "blue", "yellow"}
# print("\n\nQuestion 7")
# if color1 in primary_colors and color2 in primary_colors and color3 in primary_colors:
#   print("All primaqry colors")
# else:
#   print("Not all primary colors")

# You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". Write an if statement that prints "Manual mode activated" if mode is "manual", "Automatic mode activated" if mode is "automatic", and "System is off" if mode is "off".
# mode = input("Enter a mode: ").lower()
# print("\n\nQuestion 8")
# if mode == "manual":
#   print("Manual mode activated")
# elif mode == "automatic":
#   print("Automatic mode activated")
# elif mode == "off":
#   print("System is off")
# else:
#   print("Invalid mode")

# Given a string `message` entered by the user, use if statements to check if the message contains any of the words "urgent", "important", or "immediate". If it contains any of these words, print "High priority message". Otherwise, print "Normal message".
# message = input("Enter a message: ")
# message_entered = message.lower() 
# print("\n\nQuestion 9")
# if "urgent" in message_entered or "important" in message_entered or "immediate" in message_entered:
#   print("High priority message")
# else:
#   print("Normal message")

#  10.	You have two variables, status1 and status2, provided through user input, each of 
# 	which can be "active", “inactive", or "pending". Write an if statement to print 
# 	"Both active" if both statuses are "active", "One active" if exactly one is "active",
# 	and "None active" if neither is "active".
# status2 = input("Enter second status (active/inactive/pending): ").lower().strip()
# status1 = input("Enter first status (active/inactive/pending): ").lower().strip()
# print("\n\nQuestion 10")
# if status1 == "active" and status1 == "active":
#     print("Both active")
# elif (status1 == "active") or (status1 == "active"):
#     print("One active")
# else:
#     print("None active")

#  11. 	Given a string `filename` supplied by the user, write an if statement to check if the
# 	filename ends with “.jpg", ".png", or ".gif". Print "Image file" if it does, otherwise
# 	print "Not an image file".
# Get the filename from the user
# filename = input("Enter the filename: ").lower().strip()
# print("\n\nQuestion 11")
# if filename.endswith((".jpg", ".png", ".gif")):
#     print("Image file")
# else:
#     print("Not an image file")


#  12. 	You have a variable `access_level` provided through user input which can be "admin",
# 	"user", or "guest". Write an if statement that prints "Full access" if access_level is
# 	"admin", "Limited access" if it is "user", and "No access" if it is "guest".
# Get user input
# access_level = input("Enter access level (admin/user/guest): ").lower().strip()
# print("\n\nQuestion 12")
# if access_level == "admin":
#     print("Full access")
# elif access_level == "user":
#     print("Limited access")
# elif access_level == "guest":
#     print("No access")
# else:
#     print("Invalid access level")



#  13. 	Given a string `email` collected from the user, write an if statement to check if the
# 	email contains both "@" and 	"." characters. Print "Valid email" if it does, otherwise
# 	print "Invalid email".
# Get the email input from the user
# email = input("Enter your email address: ")
# print("\n\nQuestion 13")
# if "@" in email and "." in email:
#     print("Valid email")
# else:
#     print("Invalid email")


#  14. 	You have a variable `day` provided by user input which can be any day of the week 
# 	(e.g., "Monday", "Tuesday", 	etc.). Write an if statement that prints "Weekend" if the
# 	day is "Saturday" or "Sunday", and "Weekday" if it is any other day.
# Get the day input from the user
# day = input("Enter the day of the week: ").capitalize()
# print("\n\nQuestion 14")
# if day == "Saturday" or day == "Sunday":
#     print("Weekend")
# else:
#     print("Weekday")


#  15. 	Write a program that takes three numbers (num1, num2, num3) as a comma-separated string 
# 	input from the user and prints the greatest number. Use conditional statements
# 	to determine which number is the greatest. Bonus point if you can do it without `else` 
# 	statements.
nums = (input("Enter three numbers separated by commas: "))
num1, num2, num3 = nums.split(',')
greatest = num1
print("\n\nQuestion 15")
if num2 > greatest:
    greatest = num2
if num3 > greatest:
    greatest = num3
print("The greatest number is:", greatest)





