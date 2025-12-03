# 3. Write a program that generates a random secret number between 1 and 50. Use a while loop to allow 
#    the user to guess the number with a maximum of 5 attempts. Provide hints if the guess is too high or too low. E.g. if the secret num is 35, and the user guesses 42, their guess is too high. If they guess lower than 35, their guess is too low.

# while True:

#     secret_number = 35 
#     attempt = 0
#     maximum_try = 5
#     print("Guess the secret number between 1 and 50. You can only guess 5 times!")
#     while attempt < maximum_try:
#         response = int(input("Guess the secret number: ")) 
#         attempt += 1
#         if attempt == maximum_try:
#             print("oops you have reach your maximum attempt. Quit")
#         elif response == secret_number:
#             print("congratulations you guessed right")
#             break
#         elif response < secret_number:
#             print("Your guess is too low, try higher numbers")
#         elif response > secret_number:
#             print("Your guess is too high, try a lower number")
#     replaying = input("do you want to play again?: ").lower() 
#     if replaying != "yes":
#         print("Thanks for playing! Goodbye")
#         break


# import random

# while True:
#     secret_number = random.randint(1, 50)
#     attempts = 0
#     max_attempts = 5

#     print("Guess the secret number between 1 and 50. You have 5 attempts!")

#     while attempts < max_attempts:
#         user_input = input("Enter your guess: ")

#         # Check if input is a number
#         if not user_input.isdigit():
#             print("Please enter a valid number between 1 and 50.")
#             continue

    #     guess = int(user_input)

    #     # Validate range
    #     if guess < 1 or guess > 50:
    #         print("Your guess must be between 1 and 50.")
    #         continue

    #     attempts += 1

    #     if guess == secret_number:
    #         print("Congratulations! You guessed the correct number!")
    #         break
    #     elif guess > secret_number:
    #         print("Too high! Try a smaller number.")
    #     else:
    #         print("Too low! Try a larger number.")

    #     if attempts == max_attempts:
    #         print(f"Sorry, you've used all {max_attempts} attempts. The secret number was {secret_number}.")

    # # Ask if the user wants to play again
    # play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    # if play_again != "yes":
    #     print("Thanks for playing! Goodbye")
    #     break

# 4. Write a program that keeps asking the user for a password until they enter the correct one. The correct password is `secret`.
# while True:
#     password = "secret"
#     entry = input("enter the password: ")
#     if entry == password:
#         print("Amazing! you got the password") 
#         break
#     elif not entry.isalpha():
#         print("Entry must be alphabet")
#     else:
#         print("invalid entry, try again")


# # 8. Write a program that takes a string input from the user and uses a while loop to count the number of vowels (a, e, i, o, u) in the string.

# text = input("Enter a string: ").lower()
# i = 0
# vowel_count = 0
# vowels = "aeiou"

# while i < len(text):
#     if text[i] in vowels:
#         vowel_count += 1
#     i += 1
# print("Number of vowels:", vowel_count)

 

# 9. Write a program that takes a string input from the user and uses a while loop to reverse the string.
# Do not use slicing or reversed().
# Take input from the user
    
# text = input("Enter a string: ")
# i = len(text) - 1
# reversed_text = ""

# # Use while loop to reverse the string
# while i >= 0:
#     reversed_text += text[i]
#     i -= 1

# # Display the reversed string
# print("Reversed string:", reversed_text)

# 10. Write a program that takes comma-separated integers from the user, converts that
# 	to a tuple and uses a while loop to find the minimum value in the tuple. Do not 
#   Use the min() function.

# Take input from the user
# numbers = input("Enter comma-separated integers: ")

# Convert input string to tuple of integers
# num_tuple = tuple(int(x) for x in numbers.split(','))

# Initialize variables
# i = 1
# minimum = num_tuple[0]

# # Use while loop to find the minimum value
# while i < len(num_tuple):
#     if num_tuple[i] < minimum:
#         minimum = num_tuple[i]
#     i += 1

# # Display the result
# print("The minimum value in the tuple is:", minimum)



# 11. Write a program that takes a string input from the user and uses a while loop to count
#     the occurrences of each character, storing the counts in a dictionary.
# Sample Input:
# Enter a string: Hello
# Sample Output:
# {‘h’: 1, ‘e’: 1, ‘l’: 2, ‘o’: 1}
# Take input from the user
# text = input("Enter a string: ")

# Initialize variables
# i = 0
# char_count = {}

# # Use while loop to count occurrences
# while i < len(text):
#     char = text[i]
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
#     i += 1

# # Display the result
# print("Character occurrences:")
# print(char_count)


# second assignment

# 2. Write a program that simulates a grocery store checkout. The user should enter the prices of items until they decide to stop. The program should calculate and display the total cost.
# Sample Input and Output:
# Enter item price: 2.99
# Enter another item? (yes/no): yes
# Enter item price: 5.49
# Enter another item? (yes/no): no
# Total cost: 8.48

# Initialize total cost
# total_cost = 0.0

  
# print("Welcome to the Grocery Store Checkout!")
# print("Enter the price of each item.")
# print("Type 'done' when you are finished.\n")


# while True:
#     price = input("Enter item price (or 'done' to finish): ")

#     if price.lower() == "done":
#         break  
    
#     try:
#         total_cost += float(price)
#     except ValueError:
#         print("Invalid input! Please enter a valid number.")

# print("\nCheckout complete.")
# print(f"Total cost of all items: ₦{total_cost:.2f}")


# # 3. Write a program that continuously prompts the user to enter a password until they enter a valid one. A valid password must be at least 8 characters long and have a maximum of 25 characters.
# # Sample Input and Output:
# # Enter password: hello
# # Password must be at least 8 characters long and have a maximum of 25 characters.
# # Enter password: mysecretpasswordisasecret
# # Password accepted.

# # Continuously prompt for a valid password
# while True:
#     password = input("Enter your password: ")

#     # Check password length
#     if len(password) < 8:
#         print("Password too short! It must be at least 8 characters long.\n")
#     elif len(password) > 25:
#         print("Password too long! It must not exceed 25 characters.\n")
#     else:
#         print("Password accepted!")
#         break


#  4.	Write a program that asks for the user's age and keeps prompting them until they 
# 	enter a valid age (greater than or equal to 0).
# 	Sample Input and Output:
# 	Enter your age: -5
# 	Invalid age. Please enter a valid age.
# 	Enter your age: 25
# 	Age accepted.

# Continuously prompt for a valid age
# while True:
#     try:
#         age = int(input("Enter your age: "))
        
#         if age >= 0:
#             print("Thank you! Your age is:", age)
#             break
#         else:
#             print("Invalid input! Age cannot be negative.\n")
#     except ValueError:
#         print("Invalid input! Please enter a valid number.\n")


#  5. 	Write a program that tracks the inventory of items in a store. The user should be able to add or remove items and the program should display the current inventory after each operation. The program stops when the user decides to exit.
# 	The current store inventory is {‘eggs’: 40, ‘fish’: 200, ‘bread’: 343, ‘yam’:2}
# 	Sample Input and Output:
# 	Enter operation (add/remove/exit): add
# Enter item: eggs
# Enter quantity: 10
# Current inventory: {'eggs': 50, 'fish': 200, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): remove
# Enter item: fish
# Enter quantity: 50
# Current inventory: {'eggs': 50, 'fish': 150, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): exit


inventory = {'eggs': 40, 'fish': 200, 'bread': 343, 'yam': 2}

print("Welcome to the Store Inventory System!")
print("Current Inventory:", inventory)
print("\nYou can perform the following actions:")
print("1. Add item")
print("2. Remove item")
print("3. View inventory")
print("4. Exit\n")

while True:
    action = input("Enter your choice (add/remove/view/exit): ").lower()

    if action == "add":
        item = input("Enter the item name: ").lower()
        quantity = int(input("Enter the quantity to add: "))

        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity

        print(f"{quantity} {item}(s) added successfully.")
        print("Updated Inventory:", inventory, "\n")

    elif action == "remove":
        item = input("Enter the item name: ").lower()
        if item in inventory:
            quantity = int(input("Enter the quantity to remove: "))

            if quantity >= inventory[item]:
                del inventory[item]
                print(f"All {item}(s) removed from inventory.")
            else:
                inventory[item] -= quantity
                print(f"{quantity} {item}(s) removed successfully.")
        else:
            print("Item not found in inventory.")

        print("Updated Inventory:", inventory, "\n")

    elif action == "view":
        print("Current Inventory:", inventory, "\n")

    elif action == "exit":
        print("Exiting inventory system... Goodbye!")
        break

    else:
        print("Invalid choice! Please enter add, remove, view, or exit.\n")

