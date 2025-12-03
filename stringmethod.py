# -------------------------------- .LOWER() --------------------------------
# 1. Create a word in uppercase and print it in lowercase.
# Example:
word = "ELEPHANT"
word_lower = word.lower()
print("word:", word)
print("word_lower:", word_lower)
# Expected output:
# elephant

# -------------------------------- .CAPITALIZE() --------------------------------
# 2. Create a sentence in any case and print it with only the first letter capitalized.
# Example:
sentence = "hELLO from school"
print(sentence.capitalize())
# Expected output:
# Hello from school

# -------------------------------- .TITLE() --------------------------------
# 3. Create a phrase with spaces, hyphens, or underscores and print it in title case.
# Example:
phrase = "fresh-juice_day"
phrase = phrase.replace("-", " ").replace("_", " ")
print(phrase.title())
# Expected output:
# Fresh Juice Day

# -------------------------------- .COUNT() --------------------------------
# 4. Create a text and print how many times "banana" appears.
# Example:
text = "banana banana banana"
print(text.count("banana"))
# Expected output:
# 3

# -------------------------------- .STARTSWITH() AND .ENDSWITH() --------------------------------
# 5. Create a string and print True if it starts with a specific prefix "super", else False.
# Example:
text = "superhero"
print(text.startswith("super"))
# Expected output:
# True

# 6. Create another string and print True if it ends with a specific suffix ".txt", else False.
# Example:
text = "notes.txt"
print(text.endswith(".txt"))
# Expected output:
# True

# -------------------------------- COMBINED TASK --------------------------------
# 7. Create a filename and print True if it ends with ".jpg", ".png", or ".gif" (case-insensitive).
# Example:
filename = "holiday.PnG"
image_file_extension = (".jpg", ".png", ".gif")
print(filename.lower().endswith(image_file_extension))
# Expected output:
# True

# -------------------------------- EXTRA TASK --------------------------------
# 8. Create a short message in uppercase and print it in lowercase, capitalized, and title case — one per line.
# Example:
message = "WELCOME TO THE EVENT"
print(message.lower())
print(message.capitalize())
print(message.title())
# Expected output:
# welcome to the event
# Welcome to the event
# Welcome To The Event