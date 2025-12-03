# # 1. Write a function sum_numbers(a, b) that returns the sum of two numbers.
# # def sum_numbers(a, b):
# #     return a + b
# # print(sum_numbers(2,3))

# # 2. Write a function is_even(n) that returns True if n is even and False if n is odd.
# # def is_even(n):
# #     return n % 2 == 0
# # print(is_even(9))

# # 3. Write a function is_prime(n) that returns True if n is a prime number and False otherwise.
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# print(is_prime(7))   # True
# print(is_prime(31))  # False

# 4. Using the is_prime(n) function from number 3, write a function that asks a user for an input n and returns all the prime numbers up to n.
# def is_prime(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0:
#         return False
#     i = 3
#     while i * i <= n:
#         if n % i == 0:
#             return False
#         i += 2
#     return True

# def primes_up_to_user_input():
#     n = int(input("Enter a positive integer: "))
#     primes = []
#     for i in range(2, n + 1):
#         if is_prime(i):
#             primes.append(i)
#     print("Prime numbers up to", n, "are:", primes)

# primes_up_to_user_input()

# 5. Write a function lesser_of_two_evens(a, b) that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd.
# def lesser_of_two_evens(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         return min(a, b)
#     else:
#         return max(a,b)
    
# print(lesser_of_two_evens(4, 8))  
# print(lesser_of_two_evens(3, 8))  
# print(lesser_of_two_evens(7, 5)) 

# 6. Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if both words begin with the same letter.
# is_alliteration(‘Levelheaded llama’) —> True
# is_alliteration(‘Crazy Kangaroo’) –> False

# def is_alliteration(two_word_string: str):
#     two_word_strings = two_word_string.lower().split()
#     return two_word_strings[0][0] == two_word_strings[1][0]
# print(is_alliteration("Levelheaded llama"))
# print(is_alliteration("Crazy Kangaroo"))


# 7. Write a function old_macdonald(name) that capitalizes the first and fourth letters of a name
# old_macdonald(‘macdonald’) —> MacDonald
# Note: ‘macdonald’.capitalize() returns Macdonald, not MacDonald.

# def old_macdonald(name: str):
#     name_cap = name[0].upper() + name[1:3] + name[3].upper() + name[4:]
#     return name_cap
# print(old_macdonald("macdonald"))

# 8. Write a function spy_game(list_of_ints) that takes in a list of integers and returns True if it contains 007 in order.
# spy_game([1, 2, 4, 0, 0, 7, 5]) —> True
# spy_game([1, 0, 2, 4, 0, 5, 7]) —> True
# spy_game([1, 7, 2, 0, 4, 5, 0]) —> False

# def spy_game(list_of_ints):
#     nums = [0, 0, 7]
#     position_of_nums = 0
#     for num in list_of_ints:
#         if num == nums[position_of_nums]:
#             position_of_nums += 1
#         if position_of_nums == len(nums):
#             return True
#     return False
# print(spy_game([1, 2, 4, 0, 0, 7, 5]))
# print(spy_game([1, 7, 2, 0, 4, 5, 0]))

# 9. Write a function vol(radius) that computes the volume of a sphere given its radius.
# import math

# def vol(radius):
#     return (4/3) * math.pi * radius**3

# print(vol(3))
# print(vol(5))  

# # 10. Write a function range_check(num, low, high) that checks whether a number is in a given range (inclusive of high and low).

# def range_check(num, low, high):
#     return low <= num <= high
# print(range_check(3, 5, 10))   # False
# print(range_check(5, 1, 10))   # True
# print(range_check(1, 1, 10))   # True (inclusive)
# print(range_check(10, 1, 10))  # True (inclusive)
# print(range_check(0, 1, 10))   # False
# print(range_check(15, 1, 10))  # False

# 11. Write a function upper_lower(text) that accepts a string and calculates the number of uppercase letters and lowercase letters.

# def upper_lower(text: str):
#     no_of_upper_case_letter = 0
#     no_of_lower_case_letter = 0
#     for char in text:
#         if char.isupper():
#             no_of_upper_case_letter += 1
#         elif char.islower():
#             no_of_lower_case_letter += 1
#     return no_of_lower_case_letter, no_of_upper_case_letter
# print(upper_lower("MarAdona"))


# 12. Write a function unique_list(list_items) that takes in a list and returns a new list with unique elements of the first list. Do not use the set() constructor.

# def unique_list(list_items):
#     unique_list = []
#     for item in list_items:
#         if item not in unique_list:
#             unique_list.append(item)
#     return unique_list
# print(unique_list([1, 2, 2, 3, 4, 4, 5]))

#  13.	Write a function multiply(list_items) to multiply all the numbers in a list.
# 	Sample List: [1, 2, 3, -4]
# 	Expected output: -24

def multiply(list_items):
    for item in list_items:

        return list_items[0] * list_items[1] * list_items[2] * list_items[3]
print(multiply([1, 2, 3]))

#  14. 	Write a function is_pangram(text) to check whether a string is a pangram or not. 
# 	Note: A pangram is a word or sentence that contains every letter of the alphabet at  
# 	least once. For example: “The quick brown fox jumps over the lazy dog”.
# # 	Hint: Import and use the string module.
# import string
# def is_pangram(text: str):
#     text = text.lower()
#     for char in string.ascii_lowercase:
#         if char not in text:
#             return False
#     return True
# print(is_pangram("The quick brown fox jumps over the lazy dog"))
# print(is_pangram("Hello world"))

#  15. 	Write a function are_anagrams(s1, s2) that checks if two strings are anagrams of each
# 	other. a word, phrase, or name formed by rearranging the letters of another, such as
# 	spar, formed from rasp.

# def are_anagrams(s1, s2):
#     s1_clean = s1.replace(" ", "").lower()
#     s2_clean = s2.replace(" ", "").lower()
#     return sorted(s1_clean) == sorted(s2_clean)
# print(are_anagrams("spar", "rasp"))          
# print(are_anagrams("listen", "silent"))     
# print(are_anagrams("hello", "world"))       
# print(are_anagrams("Dormitory", "Dirty room")) 

#  16. Write a function calculate_bmi(weight, height) that calculates the Body Mass Index 
# 	(BMI) given weight in kilograms and height in meters.

# def calculate_bmi(weight, height):
#     return weight/height**2
# print(calculate_bmi(90, 1.68))

#  17. 	Write a function calculate_simple_interest(principal, rate, time) that calculates the 
# 	simple interest given principal amount, interest rate, and time (in years).

# def calculate_simple_interest(principal, rate, time):
#     interest = (principal * rate * time) / 100
#     return interest
# print(calculate_simple_interest(1000, 5, 3))  
# print(calculate_simple_interest(2000, 7.5, 2)) 