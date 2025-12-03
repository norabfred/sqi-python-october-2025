# 1. Print numbers from 1 to 5
# i = 1
# while i <=5:
#     print(i)
#     i += 1
# Expected Output:
# 1
# 2
# 3
# 4
# 5


# 2. Print "Hello" 3 times
# i = 1
# while i <= 3:
#     print("Hello")
#     i += 1

# Expected Output:
# Hello
# Hello
# Hello


# 3. Print only even numbers from 2 to 10 (do not use += 2)
# i = 2
# while i <= 10:
#     if i % 2 == 0:
#         print(i)
#     i += 1
# Expected Output:
# 2
# 4
# 6
# 8
# 10


# 4. Print numbers in reverse from 5 to 1 using a while loop.
# i = 5
# while i >= 1:
#     print(i)
#     i -= 1
# Expected Output:
# 5
# 4
# 3
# 2
# 1



#  5.	Print numbers from 1 to 10, but skip number 5 - do not use "continue" statement. 
# i = 1
# while i <= 10:
#     if i == 5:
#         i += 1
#     else:
#         print(i)
#         i += 1
# Expected Output:
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10



#  6. 	Print a square of stars
# Ask the user to enter a number
# stars = int(input("Enter a number: "))
# i = 1
# while i <= stars:
#     print("*" * stars)
#     i += 1

# Example 1:
# Input: 3

# Output:
# ***
# ***
# ***

# Example 2:
# Input: 5

# Output:
# *****
# *****
# *****
# *****
# *****


#  7. Print a right triangle of stars
# Ask the user to enter a number
# triangle = int(input("Enter the length of triangle: "))
# i = 1
# while i <= triangle:
#     print("*" * i)
#     i += 1
# Example:
# Input: 4

# Output:
# *
# **
# ***
# ****



#  8. 	Print a countdown
# Ask the user to enter a number where they want to start the countdown from.
# Ask the user to enter a number to start the countdown
# number = int(input("Enter a number to start the countdown: "))
# while number > 0:
#     print(number)
#     number -= 1
# print("Go!")

# Example:
# Input: 5

# Output:
# 5
# 4
# 3
# 2
# 1
# Go!


#  9. 	Print "1" ten times on the same line using a while loop
# i = 1
# while i <= 10:
#     print("1", end="")
#     i += 1


# Expected Output:
# 1111111111


# 10.  Print a list of the first 12 multiples of 3 starting from 3
# multiples = []
# i = 1
# while i <= 12:
#     multiples.append(3 * i)
#     i += 1
# print(multiples)


# # second assignment

# Write a program that uses a while loop to print numbers from 1 to 10.
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# Write a program that takes an integer n from the user and calculates the sum of all 
# natural numbers up to n using a while loop. e. G if n is 5, do 1+2+3+4+5 (15).
# Ask the user to enter a number
# n = int(input("Enter a number: "))
# i = 1
# total = 0
# result = []

# while i <= n:
#     result.append(str(i))
#     total += i
#     i += 1
# print(" + ".join(result) + " = " + str(total))

# # # 
# integer = int(input("Enter an integer: "))
# while integer > 0:
#     print(integer)
#     integer -= 1


# Ask the user to enter a number
# n = int(input("Enter a number to start the countdown: "))

# while n >= 0:
#     print(n)
#     n -= 1


# Write a program that takes an integer n from the user and uses a while loop to print all even numbers from 1 to n.
# n = int(input("Enter any number: "))
# i = 1
# while i <= n:
#     if i % 2 == 0:
#         print(i)
#     i += 1
 
# Write a program that takes two integers, base and exponent, from the user and uses a while loop to calculate base raised to the power of exponent.
# base = int(input("Enter a number: "))
# exponent = int(input("Enter another number: "))
# result = base ** exponent
# i = 1 
# while i <= result:
#     i += 1
#     print(f"{result}", end="")



# height = int(input("Enter a number: "))
# i = 1

# while i <= height:
#     print("*" * height)
#     height -= 1

