# # Scenario: You need to check if a user's password is strong enough.

# # Task: Write a program in a file named `password_strength_checker.py` that takes a string called `password` and prints `True` if the password is strong and `False` otherwise. A strong password:
# password = "Password123!"

# # Is at least 8 characters long.
# # has_at_least_8_char = len(password) >= 8 
# # # print(has_at_least_8_char)
# # # Contains both uppercase and lowercase characters.
# # has_both_cases = any(char.islower() for char in password) and any(char.isupper() for char in password)
# # # print(has_both_cases)

# # # Contains at least one digit.
# # has_digit = [char.isdigit() for char in password]
# # # print(any(has_digit))

# # # Contains at least one special character (e.g., !@#$%^&*()).
# # contain_at_a_least_special_char = [char in "!@#$%^&*()" for char in password]
# # # print(any(contain_at_a_least_special_char))

# # chaining the boolean
# # print(has_at_least_8_char and has_both_cases and has_digit and contain_at_a_least_special_char for char in password)


# # Tip: Check for True or False for each condition of a strong password and chain the boolean results of each of them. If they are all True, the boolean chaining will result to True and result to False if there is at least one False.

# # DO NOT USE REGEX.


# # ................................WINNIES'S CORRECTION.................................................
# # ---------------PASSWORD STRENGTH CHECKER ASSIGNMENT CORRECTION----------------------


# # Scenario: You need to check if a user's password is strong enough.

# # Task: Write a program in a file named `password_strength_checker.py` that takes a string called `password` and prints `True` if the password is strong and `False` otherwise. A strong password:

# # Is at least 8 characters long.
# # Contains both uppercase and lowercase characters.
# # Contains at least one digit.
# # Contains at least one special character (e.g., !@#$%^&*()).

# # Tip: Check for True or False for each condition of a strong password and chain the boolean results of each of them. If they are all True, the boolean chaining will result to True and result to False if there is at least one False.

# # DO NOT USE REGEX.

# # password = "Password@"
# # has_at_least_8_chars = len(password) >= 8
# # print("has_at_least_8_chars:", has_at_least_8_chars)

# # has_upper = any(char.isupper() for char in password)
# # print("has_upper:", has_upper)

# # has_lower = any(char.islower() for char in password)
# # print("has_lower:", has_lower)

# # has_digit = any(char.isdigit() for char in password)
# # print("has_digit:", has_digit)

# # special_chars = "!@#$%^&*()"
# # has_special_char = any(char in special_chars for char in password)

# # print("has_special_char:", has_special_char)

# # print("Result:", has_at_least_8_chars and has_upper and has_lower and has_digit and has_special_char)
# # print("Result:", all([has_at_least_8_chars, has_lower, has_upper, has_digit, has_special_char]))

# # password = "asswor"

# # has_at_least_8_chars = len(password) >= 8

# # has_upper = False
# # has_lower = False
# # has_digit = False
# # has_special_char = False

# # special_chars = "!@#$%^&*()"

# # for char in password:
# #     if char.isupper() and not has_upper:
# #         has_upper = True
# #     elif char.islower() and not has_lower:
# #         has_lower = True
# #     elif char.isdigit() and not has_digit:
# #         has_digit = True 
# #     elif char in special_chars and not has_special_char:
# #         has_special_char = True


# # has_at_least_8_chars = len(password) >= 8
# # print("has_at_least_8_chars:", has_at_least_8_chars)

# # has_upper = any(char.isupper() for char in password)
# # print("has_upper:", has_upper)

# # has_lower = any(char.islower() for char in password)
# # print("has_lower:", has_lower)

# # has_digit = any(char.isdigit() for char in password)
# # print("has_digit:", has_digit)

# # special_chars = "!@#$%^&*()"
# # has_special_char = any(char in special_chars for char in password)

# # print("has_special_char:", has_special_char)

# # print("Result:", has_at_least_8_chars and has_upper and has_lower and has_digit and has_special_char)
# # print("Result:", all([has_at_least_8_chars, has_lower, has_upper, has_digit, has_special_char]))



# # ---------------PASSWORD STRENGTH CHECKER ASSIGNMENT CORRECTION----------------------



# # ---------------FUNCTION DEMO----------------------
# def is_password_strong(password):

#     has_at_least_8_chars = len(password) >= 8

#     has_upper = False
#     has_lower = False
#     has_digit = False
#     has_special_char = False

#     special_chars = "!@#$%^&*()"

#     for char in password:
#         if char.isupper() and not has_upper:
#             has_upper = True
#         elif char.islower() and not has_lower:
#             has_lower = True
#         elif char.isdigit() and not has_digit:
#             has_digit = True 
#         elif char in special_chars and not has_special_char:
#             has_special_char = True


#     has_at_least_8_chars = len(password) >= 8

#     has_upper = any(char.isupper() for char in password)

#     has_lower = any(char.islower() for char in password)

#     has_digit = any(char.isdigit() for char in password)

#     special_chars = "!@#$%^&*()"
#     has_special_char = any(char in special_chars for char in password)
#     return has_at_least_8_chars and has_upper and has_lower and has_digit and has_special_char



# passwords = ["MyStrongSecretPass", "Password&123", "HelloFromPython@123"]
# for password in passwords:
#     print(is_password_strong(password))






# # ................................WINNIES'S CORRECTION.................................................
 




