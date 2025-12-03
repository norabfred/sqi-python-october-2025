# .................................second assignment.................................................


# --------------------------------LIST COMPREHENSION & GENERATORS EXERCISES--------------------------------
# 1. Create a list of the square of each number
# Input: [1, 2, 3, 4, 5]
# Expected Output: [1, 4, 9, 16, 25]
# digits = [1, 2, 3, 4, 5]

# print("\n\nQuestion 1")
# list_of_squares = []
# for digit in digits:  # 1, 2, 3
#     list_of_squares.append(digit * digit)
# print(list_of_squares)


# 2. Create a list of names that contain the letter 'a'
# Input: ["John", "Sara", "Mike", "Amanda"]
# # Expected Output: ["Sara", "Amanda"]
# names = ["John", "Sara", "Mike", "Amanda"]
# print("\n\nQuestion 2")
# has_letter_a = [name for name in names if "a" in name]
# print(has_letter_a)


# 3. Create a list of Booleans indicating if each number is greater than 10
# Input: [5, 12, 3, 18, 7]
# Expected Output: [False, True, False, True, False]
# values = [5, 12, 3, 18, 7]
# print("\n\nQuestion 3")
# print([num > 10 for num in values])


# 4. Create a list of the last characters of each word
# Input: ["dog", "cat", "lion", "tiger"]
# Expected Output: ["g", "t", "n", "r"]
# animals = ["dog", "cat", "lion", "tiger"]
# print("\n\nQuestion 4")
# last_char = [animal[-1] for animal in animals]
# print(last_char)


# 5. Are all the numbers greater than 10?
# Input: [5, 12, 3, 18, 7]
# Expected Output: False
# values = [5, 12, 3, 18, 7]
# print("\n\nQuestion 5")
# print(all(value > 10 for value in values))


# 6. Is there any name that contains the letter 'a'?
# Input: ["John", "Sara", "Mike", "Amanda"]
# # Expected Output: True
# names = ["John", "Sara", "Mike", "Amanda"]
# print("\n\nQuestion 6")
# print(any(name for name in names if "a" in name))


# 7. Are all the words made up of only uppercase letters?
# Input: ["HELLO", "world", "pyTHon", "ROCKS"]
# Expected Output: False
# greetings = ["HELLO", "world", "pyTHon", "ROCKS"]
# print("\n\nQuestion 7")
# print(all(greeting.isupper() for greeting in greetings))


# 8. Is there any word that starts with 'z'?
# Input: ["apple", "zebra", "mango", "lemon"]
# Expected Output: True
# words = ["apple", "zebra", "mango", "lemon"]
# print("\n\nQuestion 8")
# # print(any(word.startswith("z") for word in words))
# print(any(word for word in words if word.lower().startswith("z")))


# 9. Is there any email address that contains ".org"?
# Input: ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]
# Expected Output: True
# emails = ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]
# print("\n\nQuestion 9")
# print(any(email for email in emails if ".org" in email))

# 10. Are all numbers odd?
# # Input: [1, 3, 5, 7, 9]
# # Expected Output: True
# values = [1, 3, 5, 7, 9]
# print("\n\nQuestion 10")
# print(all(value for value in values if value % 2 != 0))


# 11. Are all words longer than 2 characters?
# Input: ["hi", "dog", "go", "sun"]
# Expected Output: False
# words = ["hi", "dog", "go", "sun"]
# # print("\n\nQuestion 11")
# print(all(len(word) > 2 for word in words))


# 12. Create a list of triple the value of each number
# Input: [2, 4, 6, 8]
# Expected Output: [6, 12, 18, 24]
# nums = [2, 4, 6, 8]
# triples = []
# print("\n\nQuestion 12")
# for num in nums:
#     triples.append(num * 3)
# print(triples)


# 13. Are all temperatures above 0°C?
# Input: [12, 7, 3, -1, 5]
# Expected Output: False
# temperatures = [12, 7, 3, -1, 5]
# print("\n\nQuestion 13")
# print(all(temperature > 0 for temperature in temperatures))

# 14. Do all words end with a vowel?
# Input: ["banana", "mango", "kiwi", "grape"]
# Expected Output: True
# fruits = ["banana", "mango", "kiwi", "grape"]
# print("\n\nQuestion 14")
# print(all(fruit in "aeiou" for fruit in fruits ))

# 15. Create a list of words in lowercase
# Input: ["HELLO", "WORLD", "PYTHON"]
# # Expected Output: ["hello", "world", "python"]
# greetings = ["HELLO", "WORLD", "PYTHON"]
# lower_case = [greeting.lower() for greeting in greetings]
# print("\n\nQuestion 15")
# print(lower_case)


# 16. Is there any number less than 0?
# Input: [5, -2, 3, 0, 8]
# Expected Output: True
numbers = [5, 4, 3, 3, 8]
print("\n\nQuestion 16")
print(any(num < 0 for num in numbers))


# 17. Create a list of words that contain the letter 'e'
# Input: ["sky", "tree", "rock", "stone"]
# Expected Output: ["tree", "stone"]
items = ["sky", "tree", "rock", "stone"]


# 18. Are all names starting with uppercase letters?
# Input: ["Alice", "Bob", "charlie", "David"]
# Expected Output: False
names = ["Alice", "Bob", "charlie", "David"]


# 19. Is there any sentence longer than 20 characters?
# Input: ["Short one", "This is a much longer sentence", "Okay"]
# Expected Output: True
sentences = ["Short one", "This is a much longer sentence", "Okay"]

# --------------------------------LIST COMPREHENSION & GENERATORS EXERCISES--------------------------------
