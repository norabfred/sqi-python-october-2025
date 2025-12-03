# # ..............................ASSIGNMENT................................................

# # 1. Write a program that takes an integer input from the user and uses a loop to calculate 
# # the sum of its digits. Print the sum. Example:
# # Input: 1234
# # Output: 10 (1+2+3+4)

# # collect users input
# # go through the numbers entered
# # add the numbers together 

# numbers = (input("Enter a number: "))
# sum_of_digits = 0
# digit = " + ".join(numbers)

# for number in numbers:
#     sum_of_digits += int(number)
# print("The sum of the digits is:", sum_of_digits)
# print(f"{sum_of_digits} ({digit})")



# # 2. Collect a string from the user and use loops to count the number of vowels and consonants in the string. Print the counts. Example:
# # Input: "hello world"
# # Output: Vowels: 3, Consonants: 7
# # pseudo codes:
# # 1. collect a string from the user
# # 2. go through the string provided
# # 3. count how many vowels and consonant in the string
# #  4. display the result

# # import string
# # phrase = input("Enter a phrase: ").lower()
# # vowel = "aeiou"
# # alphabets = string.ascii_lowercase
# # consonants = 0
# # vowel_conts = 0 

# # for char in phrase:
# #     if char in alphabets:
# #         if char in vowel:
# #             vowel_conts += 1
# #         else:
# #             consonants += 1
# # print(vowel_conts)
# # print(consonants)


# # 3. Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12. Example:
# # Input: 5
# # Output:
# # 5 x 1 = 5
# # 5 x 2 = 10
# # 5 x 3 = 15
# # ...
# # 5 x 12 = 60

# # number = int(input("Enter an integer: "))
# # for i in range(1, 13):
# #     print(f"{number} x {i} = {number * i}")

# # 4. Collect a string from the user and use a loop to reverse the string. Print the reversed string. Do not reverse the string using [::-1] or reversed().
# # Example:
# # Input: "python"
# # Output: "nohtyp"

# # text = input("Enter a string: ")
# # reversed_text = ""

# # for char in text:
# #     reversed_text = char + reversed_text  

# # print("Reversed string:", reversed_text)


# # 5. Write a program that takes a list of numbers (entered as comma-separated values) from the user and removes any duplicate values. Print the new list. Do not use the set() constructor. Use a loop. Example:
# # Input: "1, 2, 3, 2, 4, 3"
# # Output: [1, 2, 3, 4]
# # numbers = input("Enter comma-separated numbers: ").split(",")
# # numbers_list = list(numbers)
# # print(numbers_list)

# # empty_list = []
# # for number in numbers:
# #     if number not in empty_list:
# #         empty_list.append(number)
# # print(empty_list)

# #  6.	Write a program that takes an integer input n from the user and prints the first 
# # 	n numbers in the Fibonacci sequence. Example:
# # 	Input: 10
# # 	Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# # Program to print the first n Fibonacci numbers

# # Take input from the user
# n = int(input("Enter how many Fibonacci numbers to print: "))

# # Initialize the first two Fibonacci numbers
# a, b = 0, 1

# # Use a for loop to generate and print the sequence
# print("Fibonacci sequence:")

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b



#  7. 	Collect a list of numbers from the user (entered as comma-separated values) and use a 
# 	loop to find and print the largest number in the list. Don’t use the built-in max 
# 	function or anything similar.
# 	Input: "10, 20, 5, 15"
# 	Output: 20

# numbers = input("Enter comma-separated values: ")
# numbers_list = [int(n) for n in numbers.split(", ")]
# print(numbers_list)
# largest = numbers_list[0]

# for num in numbers_list:
#     if num > largest:
#         largest = num
# print(largest)


#  8. Write a program that takes an integer n from the user and calculates the sum of all 
# 	even numbers from 1 to n. Print the sum.
# 	Input: 10
# 	Output: 30 (2 + 4 + 6 + 8 + 10)

# n = int(input("Enter a number: "))
# total_sum = 0
# even_numbers = []
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         total_sum += i
#         even_numbers.append(str(i))
# the_numbers =  " + ".join(even_numbers)
# print(f"{total_sum} ({the_numbers}) ")


#  9. 	Collect a string from the user and use a loop to count the frequency of each character 
# 	in the string. Print each character along with its frequency. Example:
# 	Input: "hello"
# 	Output:
# h: 1
# e: 1
# l: 2
# o: 1
# collect a string from user
#  count the frequency of each character in the string
# character = input("Enter a string: ")
# frequency = {}

# for char in character:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         (frequency[char]) = 1
# for char, count in frequency.items():
#     print(f"{char}:{count}")


#  10.	Write a program that takes an integer n from the user and calculates the sum of 
# 	squares of all numbers from 1 to n. Print the sum. Example:
# 	Input: 3
# 	Output: 14 (1^2 + 2^2 + 3^2)

# n = int(input("Enter a number: "))
# sum_of_squares = 0
# calc_nums = ""
# for i in range(1, n + 1):
#     sum_of_squares += i ** 2
#     if i < n:
#         calc_nums += f"{i}^2 + "
#     else:
#         calc_nums += f"{i}^2"
    
# print(f"{sum_of_squares} ({calc_nums})")

# 11. 	Collect a phrase from the user and use a loop to generate an acronym by taking the first
# 	letter of each word. Print the acronym. Example:
# 	Input: "Portable Network Graphics"
# 	Output: "PNG"

# phrase = input("enter a phrase: ").title()
# words = phrase.split()
# acronym = ""
 
# for word in words:
#     acronym += word[0]
# print(acronym)

#  12. 	Collect a string from the user and use a loop to count the number of words in the string. 
# 	Print the count. Example:
# 	Input: "Hello world from Python"
# 	Output: 4

# phrase = input("Enter a phrase: ")
# words = phrase.split()
# count_of_words = 0
# for word in words:
#     count_of_words += 1
# print(count_of_words)

#  13. 	Collect a string from the user and only print put the words that start with the letter 
# 	‘S’. Example:
# 	Input: “Print only the words that start with s in this sentence”
# 	Output: 
# 	start
# 	s
# 	Sentence

# sentence = input("Enter a sentence: ").lower()
# letter_starwith_s = sentence.split()
# for word in letter_starwith_s:
#     if word.startswith("s"):
#         print(word)

# 14. Print all the even numbers from 1 to 20 using the range function and a loop.

# for i in range(1, 20 + 1):
#     if i % 2 == 0:
#         print(i)

# 15. Use a list comprehension to create a list of numbers between 1 and 50 that are divisible
# 	  by 3.

# numbers = []
# for i in range(1, 51):
#     if i % 3 == 0:
#         numbers.append(i)
# print(numbers)

#  or

# numbers = [i for i in range(1, 50 + 1) if i % 3 == 0]
# print(numbers)

#  16.	Go through the string below and if the length of a word is even, print that word.
# 	st = ‘Print every word in this sentence that has an even number of letters’
# 	Output: 
# 	word
# 	in
# 	this
# 	sentence
# 	that
# 	an
# 	even
# 	number
# 	of

# st = "Print every word in this sentence that has an even number of letters"
# words = st.split()
# for word in words:
#     if len(word) % 2 == 0:
#         print(word)

#  17. 	Write a program that prints the integers from 1 to 100. But for multiples of three, print 
# 	“Fizz” instead of the number, and for multiples of five, print “Buzz”. For numbers which 
# 	are multiples of both three and five, print “FizzBuzz”.

# numbers = range(1, 101)
# for i in numbers:
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)



#  18.	You are given two lists, names and grades. Print them together
# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']

# Expected Output:
# Ken got grade A
# Mia got grade E
# Rose got grade F
# Henry got grade C
# Suzan got grade B

# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']
# for i in range(len(names)):
#     print(f"{names[i]} got grade {grades[i]}")  # playful dolphin
  
#  19. Print only the items at even indexes

# items = ['shoe', 'stick', 'toy', 'fruit']
# for i in range(0, len(items), 2):
#     print(f"{i}: {items[i]}")
# Expected Output:
# 0: shoe
# 2: toy

#  20.	Given two lists of numbers of the same length, print the indices and values
#  	of where they differ in a list.

# list1 = [5, 8, 6, 7, 12, 4]
# list2 = [5, 3, 6, 9, 12, 0]
# for i in range(len(list1)):
#     if list1[i] != list2[i]:
#         print(f"Index {i}: {list1[i]} != {list2[i]}")

# Expected output:
# [
#   'Index 1: 8 != 3',
#   'Index 3: 7 != 9',
#   'Index 5: 4 != 0',
# ]

