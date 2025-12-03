# print("Hi")
# print("Hi")
# print("Hi")
# print("Hi")
# print("Hi")
# print("Hi")

# i = 1

# while i <= 6:
#     print(f"{i}: Hello")
#     # i += 1
#     i = i + 1


# i = 0

# while i < 11:
#     print(i)
#     i += 1


# i = 20

# while i >= 5:
#     print(i)
#     i -= 1


# Print all the numbers from 3 to 27
# Print all the numbers from 90 to 16
# Print all the even numbers from 8 to 24 i.e. 8, 10, 12, 14, 16, 18, 20, 22, 24

# i = 8

# while i <= 24:
#     print(i)
#     i += 2

# i = 7

# while i <= 24:
#     if i % 2 == 0:
#         print(i)
#     i += 1


# Print all the multiples of 5 between 7 and 36 i.e 10, 15, 20, 25, 30, 35

# i = 7

# while i <= 36:
#     if i % 5 == 0:
#         print(i)
#     i += 1


# Create a list of odd numbers between 5 and 40 


# i = 5
# odd_nums = []
# while i <= 40:
#     if i % 2 != 0:
#         odd_nums.append(i)
#     i += 1

# print(odd_nums)



# "1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ..., 48, 49, 50"


# i = 1
# nums = []

# while i <= 50:
#     nums.append(str(i))
#     i += 1

# nums = ", ".join(nums)
# print(nums)



# i = 1
# nums = ""

# while i <= 50:
#     nums += str(i)
#     if i != 50:
#         nums += ", "
#     # nums = nums + str(i)
#     i += 1

# print(nums)

# i = 1
# while i <= 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1 

# print("End of file")



# 7 to 17

# 7, 8, 9, 10, 11, 12, 

# i = 7
# while i <= 17:
#     print(i)
#     if i == 12:
#         break
#     i += 1


# # 7 to 17

# # 7, 8, 9, 10, 11, 13, 14, 15, 16, 17


# i = 6

# while i <= 16:
#     i += 1
#     if i == 12:
#         continue
#     print(i)

# Create a list containing 60 to 100, but stop when you get to 70 i.e. 60, 61, 62, 63, 64, 65, 66, 67, 68, 69
# Create a list containing 10 to 20, but skip 15 i.e. 10, 11, 12, 13, 14, 16, 17, 18, 19, 20



# i = 1

# while i <= 10:
#     print(i)
#     i += 1
# else:
#     print("Else running")


# i = 100

# while i <= 10:
#     print(i)
#     i += 1
# else:
#     print("Else running")



# n = int(input("Enter the value of n: "))  # 5

# i = 1
# sum_of_first_n = 0

# while i <= n:
#     sum_of_first_n += i
#     i += 1

# print(sum_of_first_n)




# ****
# ****
# ****
# ****
# ****

# length = int(input("Enter the length of the rectangle: "))
# breadth = int(input("Enter the breadth of the rectangle: "))

# i = 1
# while i <= breadth:
    # print("*" * length)
    # i += 1


# 11. Write a program that takes a string input from the user and uses a while loop to count
# the occurrences of each character, storing the counts in a dictionary.
# Sample Input:
# Enter a string: Hello
# Sample Output:
# {‘h’: 1, ‘e’: 1, ‘l’: 2, ‘o’: 1}



# --------------------------------------ASSIGNMENT CORRECTION--------------------------------------
# 1. Print numbers from 1 to 5
# Expected Output:
# 1
# 2
# 3
# 4
# 5

# i = 1
# while i <= 5:
#     print(i)
#     i += 1


# 2. Print "Hello" 3 times
# Expected Output:
# Hello
# Hello
# Hello

# i = 1

# while i <= 3:
#     print("Hello")
#     i += 1


# 3. Print only even numbers from 2 to 10 (do not use += 2)
# Expected Output:
# 2
# 4
# 6
# 8
# 10

# i = 2

# while i <= 10:
#     if i % 2 == 0:
#         print(i)
#     i += 1


# i = 1

# while i <= 5:
#     print(i * 2)
#     i += 1


# 4. Print numbers in reverse from 5 to 1 using a while loop.
# Expected Output:
# 5
# 4
# 3
# 2
# 1

# i = 5

# while i >= 1:
#     print(i)
#     i -= 1


# 5. Print numbers from 1 to 10, but skip number 5 - do not use "continue" statement. 
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

# i = 1

# while i <= 10:
#     if i != 5:
#         print(i)
#     i += 1


# i = 0

# while i <= 9:
#     i += 1
#     if i == 5:
#         continue
#     print(i)

# 6. Print a square of stars
# Ask the user to enter a number
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



# 7. Print a right triangle of stars
# Ask the user to enter a number
# Example:
# Input: 4

# Output:
# *
# **
# ***
# ****


# 8. Print a countdown
# Ask the user to enter a number where they want to start the countdown from.
# Example:
# Input: 5

# Output:
# 5
# 4
# 3
# 2
# 1
# Go!

# num = int(input("Enter a number to start the countdown from: "))

# while num >= 1:
#     print(num)
#     num -= 1
# else:
#     print("Go!")

# num = int(input("Enter a number to start the countdown from: "))

# while num >= 1:
#     if num == 2:
#         break
#     print(num)
#     num -= 1

# print("Go")


# 9. Print "1" ten times on the same line using a while loop
# Expected Output:
# 1111111111


# i = 1
# result = ""
# while i <= 10:
#     result += "1"
#     i += 1

# print(result)


# i = 1

# result = []
# while i <= 10:
#     result.append("1")
#     i += 1

# print("".join(result))


# 10. Print a list of the first 12 multiples of 3 starting from 3
# print("Hello", end="")
# print("Hi", end="")

# i = 3
# first_12_multiples_of_3 = []
# while len(first_12_multiples_of_3) != 12:
#     if i % 3 == 0:
#         first_12_multiples_of_3.append(i)
#     i += 3

# print(first_12_multiples_of_3)

# i = 3
# first_12_multiples_of_3 = []
# count = 0
# while count != 12:
#     if i % 3 == 0:
#         first_12_multiples_of_3.append(i)
#         count += 1
#     i += 3

# print(first_12_multiples_of_3)

# first_12_multiples_of_3 = []
# i = 3
# while True:
#     if i % 3 == 0:
#         if len(first_12_multiples_of_3) != 12:
#             first_12_multiples_of_3.append(i)
#         else:
#             break
#     i += 1

# print(first_12_multiples_of_3)

# 1, 2, 4, 5, 6, 7

# 1. Write a program that uses a while loop to print numbers from 1 to 10.

# 2. Write a program that takes an integer n from the user and calculates the sum of all 
# natural numbers up to n using a while loop. e. G if n is 5, do 1+2+3+4+5 (15).

# n = int(input("Enter a number: "))

# i = 1
# total = 0
# result = []
# while i <= n:
#     total += i
#     result.append(str(i))
#     i += 1

# result = f"{" + ".join(result)} = {total}"
# print(result)

# 1 + 2 + 3 + 4 + 5 = 15
# 1 + 2 + 3 + 4 + 5 + 6 = 21

# 4. Write a program that keeps asking the user for a password until they enter the correct one. The correct password is `secret`.

# from getpass import getpass

# password = ""

# while password != 'secret':
#     password = getpass("Enter the password: ").strip()
#     if password == 'secret':
#         print("Correct password")
#     else:
#         print("Incorrect password")


# password = ""

# while True:
#     password = getpass("Enter the password: ").strip()
#     if password == 'secret':
#         print("Correct password")
#         break
#     else:
#         print("Incorrect password")

# 5. Write a program that takes an integer input from the user and uses a while loop to print a countdown from that number to zero.

# 6. Write a program that takes an integer n from the user and uses a while loop to print all even numbers from 1 to n.

# 7. Write a program that takes two integers, base and exponent, from the user and uses a while loop to calculate base raised to the power of exponent.
# Sample Input:
# Enter the base: 2
# Enter the exponent: 3
# Output:
# 2 raised to the power of 3 is 8
# Sample Input:
# Enter the base: 5
# Enter the exponent: 4
# Output:
# 5 raised to the power of 4 is 625


# base = int(input("Enter the base: ")) # 2
# exponent = int(input("Enter the exponent: "))  # 5

# # 5 -> 2
# # 4 -> 2 * 2
# # 3 -> 2 * 2 * 2
# # 2
# # 1

# i = exponent
# result = 1

# while i >= 1:
#     result *= base
#     i -= 1

# print(f"{base} raised to the power of {exponent} is {result}")
# --------------------------------------ASSIGNMENT CORRECTION--------------------------------------



 
 
# --------------------------------------LOOPING THROUGH ITERABLES--------------------------------------


# name = "Deborah"

# D -> name[0]
# e -> name[1]
# b -> name[2]
# o -> name[3]
# r -> name[4]
# a -> name[5]
# h -> name[6]


# name = "Praise"

# P -> name[0]
# r -> name[1]
# a -> name[2]
# i -> name[3]
# s -> name[4]
# e -> name[5]



# name = "Deborah"
# name = "Praise"
# i = 0
# # while i <= len(name) - 1:
# while i < len(name):
#     char = name[i]
#     print(char)
#     i += 1


# sentence = "Happy new month!"
# i = 0
# # while i <= len(name) - 1:
# while i < len(sentence):
#     char = sentence[i]
#     print(char)
#     i += 1



# musical_instruments = ["guitar", "piano", "violin", "drums", "saxophone", "trumpet", "ukulele"]

# i = 0
# while i < len(musical_instruments):
#     print(musical_instruments[i])
#     i += 1



# musical_instruments = ["guitar", "piano", "violin", "drums", "saxophone", "trumpet", "ukulele"]

# i = 0
# while i < len(musical_instruments):
#     insrument = musical_instruments[i]
#     print(insrument)
#     j = 0
#     while j < len(insrument):
#         print(insrument[j])
#         j += 1
#     i += 1


# musical_instruments = ["guitar", "piano", "violin", "drums", "saxophone", "trumpet", "ukulele"]
# print(musical_instruments[0][0])

# --------------------------------------LOOPING THROUGH ITERABLES--------------------------------------

# Write a program that takes a string input from the user and uses a while loop to count the number of vowels (a, e, i, o, u) in the string.

# hello
# vowels = 2
# consonants = 3

# I am hungry
# vowels = 3
# consonants = 6


# text = input("Enter some text: ").strip().lower()

# i = 0

# vowels = 0
# consonants = 0

# while i < len(text):
#     char = text[i]
#     if char.isalpha():
#         if char in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1
#     i += 1


# print(f"Vowels: {vowels}")
# print(f"Consonants: {consonants}")


# 1. Write a program that simulates an ATM withdrawal process. The user should enter their 
# balance and then enter withdrawal amounts until they decide to stop. Ensure the user does
# not withdraw more than their balance.
# Sample Input and Output:
# Enter your balance: 500
# Enter withdrawal amount: 100
# Remaining balance: 400
# Do you want to make another withdrawal? (yes/no): yes
# Enter withdrawal amount: 50
# Remaining balance: 350
# Do you want to make another withdrawal? (yes/no): no
# Final balance: 350


# balance = int(input("Enter your balance: "))
# while True:
#     withdrawal_amt = int(input("Enter withdrawal amount: "))
#     if withdrawal_amt > balance:
#         print("Insufficient funds")
#     else:
#         balance -= withdrawal_amt
#         print(f"Remaining balance: {balance}")
    
#     another_withdrawal = input("Do you want to make another withdrawal? (yes/no): ").strip().lower()
#     if another_withdrawal != "yes":
#         print(f"Final balance: {balance}")
#         break



# balance = int(input("Enter your balance: "))
# main_loop = True
# while main_loop:
#     withdrawal_amt = int(input("Enter withdrawal amount: "))
#     if withdrawal_amt > balance:
#         print("Insufficient funds")
#     else:
#         balance -= withdrawal_amt
#         print(f"Remaining balance: {balance}")
    
#     while True:
#         another_withdrawal = input("Do you want to make another withdrawal? (yes/no): ").strip().lower()
#         if another_withdrawal == "no":
#             print(f"Final balance: {balance}")
#             main_loop = False
#             break

#         if another_withdrawal == "yes":
#             break
        
#         print("Invalid input")


# 3. Write a program that generates a random secret number between 1 and 50. Use a while loop to allow 
# the user to guess the number with a maximum of 5 attempts. Provide hints if the guess is too high or too low. E.g. if the secret num is 35, and the user guesses 42, their guess is too high. If they guess lower than 35, their guess is too low.



# 9. Write a program that takes a string input from the user and uses a while loop to reverse the string.
# Do not use slicing or reversed().

# sentence = input("Enter a sentence: ").lower().strip()  # python
# sentenced_reversed = []
# i = len(sentence) - 1
# while i >= 0:
#     sentenced_reversed.append(sentence[i])
#     i -= 1

# print("".join(sentenced_reversed))


# text = input("Enter some text: ").strip().lower()  # python
# reversed_text = ""
# i = len(text) - 1
# while i >= 0:
#     char = text[i]
#     reversed_text += char
#     i -= 1

# print(reversed_text)


# text = input("Enter some text: ").strip().lower()  # python
# reversed_text = ""
# i = 0

# while i < len(text):
#     char = text[i]
#     reversed_text = char + reversed_text
#     i += 1

# print(reversed_text)

# p
# y + p -> yp
# t + yp -> typ
# h + typ -> htyp
# o + htyp -> ohtyp
# n + ohtyp -> nohtyp

# 10. Write a program that takes comma-separated integers from the user, converts that
# to a tuple and uses a while loop to find the minimum value in the tuple. Do not 
# Use the min() function.

# numbers = tuple(input("Enter numbers separated by commas: ").split(","))

# i = 1

# min_num = int(numbers[0])

# while i < len(numbers):
#     num = int(numbers[i])
#     if num < min_num:
#         min_num = num
#     i += 1


# print(f"The smallest number is {min_num}")


# 11. Write a program that takes a string input from the user and uses a while loop to count
# the occurrences of each character, storing the counts in a dictionary.
# Sample Input:
# Enter a string: Hello
# Sample Output:
# {‘h’: 1, ‘e’: 1, ‘l’: 2, ‘o’: 1}

# text = input("Enter some text: ").strip().lower()  # hello

# occurences = {}

# i = 0

# while i < len(text):
#     char = text[i]
#     if char in occurences:
#         occurences[char] += 1
#     else:
#         occurences[char] = 1
#     i += 1



# 2. Write a program that simulates a grocery store checkout. The user should enter the prices of items until they decide to stop. The program should calculate and display the total cost.
# Sample Input and Output:
# Enter item price: 2.99
# Enter another item? (yes/no): yes
# Enter item price: 5.49
# Enter another item? (yes/no): no
# Total cost: 8.48


# total_cost = 0

# while True:
#     price = float(input("Enter item price: "))
#     total_cost += price

#     another_item = input("Enter another item? (yes/no): ").strip().lower()

#     if another_item == "yes":
#         continue

#     print(f"Total cost: {total_cost}")
#     break

# total_cost = 0

# grocery_store_loop = True

# while grocery_store_loop:
#     price = float(input("Enter item price: "))
#     total_cost += price

#     while True:
#         another_item = input("Enter another item? (yes/no): ").strip().lower()

#         if another_item == "yes":
#             break

#         if another_item == "no":
#             print(f"Total cost: {total_cost}")
#             grocery_store_loop = False
#             break

#         print("Invalid input. Enter either yes or no!")



# 3. Write a program that continuously prompts the user to enter a password until they enter a valid one. A valid password must be at least 8 characters long and have a maximum of 25 characters.
# Sample Input and Output:
# Enter password: hello
# Password must be at least 8 characters long and have a maximum of 25 characters.
# Enter password: mysecretpasswordisasecret
# Password accepted.



# 4. Write a program that asks for the user's age and keeps prompting them until they 
# enter a valid age (greater than or equal to 0).
# Sample Input and Output:
# Enter your age: -5
# Invalid age. Please enter a valid age.
# Enter your age: 25
# Age accepted.



# 5. Write a program that tracks the inventory of items in a store. The user should be able 
# to add or remove items and the program should display the current inventory after each
# operation. The program stops when the user decides to exit.
# The current store inventory is {‘eggs’: 40, ‘fish’: 200, ‘bread’: 343, ‘yam’:2}
# Sample Input and Output:
# Enter operation (add/remove/exit): add
# Enter item: eggs
# Enter quantity: 10
# Current inventory: {'eggs': 50, 'fish': 200, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): remove
# Enter item: fish
# Enter quantity: 50
# Current inventory: {'eggs': 50, 'fish': 150, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): exit


# inventory = {'eggs': 40, 'fish': 200, 'bread': 343, 'yam': 2}

# while True:
#     operation = input("Enter operation (add/remove/exit): ").strip().lower()

#     if operation not in ["add", "remove", "exit"]:
#         print("Invalid operation")
#         continue

#     if operation == "exit":
#         print("good bye 👋")
#         break

#     item = input("Enter item: ").strip().lower()
#     quantity = int(input("Enter quantity: "))
#     if quantity < 0:
#         print("Quantity must be positive")
#         continue

#     if operation == "add":
#         if item in inventory:
#             inventory[item] += quantity
#         else:
#             inventory[item] = quantity
#     elif operation == "remove":
#         if item in inventory:
#             if quantity <= inventory[item]:
#                 inventory[item] -= quantity
#             else:
#                 print(f"There are only {inventory[item]} of {item} in inventory")
#         else:
#             print("Can't remove item that is not in the inventory")
#     print(f"Current inventory: {inventory}")
# DRY - Don't Repeat Yourself