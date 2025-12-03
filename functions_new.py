# def say_hi():
#     print('hi')

# # print("Hello")

# say_hi()
# say_hi()
# say_hi()
# say_hi()
# say_hi()
# say_hi()

# [78, 793].append()


# def greet():
#     print("Good afternoon, SQI Oct Python Gurus")  # 1
#     print("inside function")  # 2


# print(greet())



# def greet():
#     print('Hello World!')  # 3

# greet()
# print('Outside function')  # 4





print("Lorem ipsum dolor")  # 1
def greet():
    print("sit amet")  # 3, 6
    print('Hello World!')  # 4, 7

print('tempor incididunt ut labore')  # 2
greet()
print("consectetur adipiscing elit")  # 5
greet()
print("Nemo enim ipsam voluptatem")  # 8


print("The sun rises in the east")  # 9


# def greet():
#     print("How's it going?")  # 1, 4, 6, 9
#     print("Stay curious, stay kind.")  # 2, 5, 7, 10


# greet()

# print("Midnight thoughts and coffee sips")  # 3
# greet()
# greet()
# print("Learning never exhausts the mind")  # 8
# greet()
# print("Wander often, wonder always")  # 11


# def square_num(num):
#     # return num ** 2
#     print(num ** 2)


# square_num(4)


# def greet1():
#     print("Hello")

# greet1("Winnie")


# def greet2(username):
#     print(username)
#     print(f"Hello, {username}!")

# greet2("Towi")

# Write a function introduction with a parameter name that prints "I am {name}".

# def add_two_nums(num1, num2):  # parameters
#     print(num1 + num2)

# add_two_nums(9, 10)  # arguments/args
# add_two_nums(2, 7)


# Write a function raise_to_power that takes in two parameters base and exponent and 
# prints base raised to the power of exponent.

# def raise_to_power(base: int, exponent: int) -> int:
#     return base ** exponent

# print(raise_to_power(2, 3))  # 8
# result = raise_to_power(2, 3)
# print(result)  # 8



# # my_list = [1, 2, 3]
# my_list = ['1', '2', '3']
# print(my_list.pop())
# # print(popped_item)
# print(my_list)



# Write a function change_to_lower with parameter word.
# Return the word lowercased.
# Print what is returned.

# Python and Javascript is dynamically typed
# Other languages like Java and C are statically typed


# type hints or type annotations

# def change_to_lower(word):
#     return word.lower()


# # print(change_to_lower("HELLO"))
# lowercase_word = change_to_lower("HELLO")
# # lowercase_word = change_to_lower(123)
# print(lowercase_word)



# Create a function upper_everyone that has parameter names which is a lit of strings where
# each istring is a name.
# Return a list of names where all the names are uppercased.

# def upper_everyone(names: list[str]) -> list[str]:
#     names.append("something")
#     return [name.upper() for name in names]

# print(upper_everyone(["Jade", "Joy", "James", "Janet", "Jack"]))

# ["JADE", "JOY", "JAMES", "JANET", "JACK"]



# nums: list[int] = [1, 2, 3]


# inventory: dict[str, int] = {"apples": 10, "bananas": 12, "oranges": 9}

# inventory: dict[str, int|str] = {"apples": 10, "bananas": 12, "oranges": "nine"}


# def greet():
#     pass


# print("Hey")



# # -----------------------------------------------ASSIGNMENT-------------------------------------------------
# 1. Create a function starts_with_m(word) that returns True if the word starts with the letter `m`.
# Otherwise, the function returns False
# Print the result of the function

# def starts_with_m(word: str):
#     return word.lower().startswith("m")

# def beginner_starts_with_m(word: str):
#     if word.lower().startswith("m"):
#         return True
#     else:
#         return False

# def intermediate_starts_with_m(word: str):
#     if word.lower().startswith("m"):
#         return True
#     return False


# print(starts_with_m("Maddie"))  # True
# print(starts_with_m("John"))  # False
# print(starts_with_m("marry"))  # True




# 2. Create a function is_even(num) that returns True if num is an even number.
# Otherwise, the function returns False
# Print the result of the function

# def is_even(num: int):
#     return num % 2 == 0

# print(is_even(3))  # False
# print(is_even(6))  # True


# 6. Write a function is_alliteration(two_word_string) that takes a two-word string and returns True if both words begin with the same letter.
# is_alliteration("Levelheaded llama") —> True
# is_alliteration("Crazy Kangaroo") –> False