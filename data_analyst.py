# Scenario:
# You are working as a data analyst for a marketing company. You have been given a large text document containing customer reviews and feedback. Your task is to extract all email addresses and phone numbers from this document for further analysis.

# Task:
# Write a Python script named `data_analyst.py` that:
# Reads the contents of a text file named reviews.txt.
# Extracts all email addresses and phone numbers from the text.
# Email addresses follow the standard format: username@domain.tld
# Phone numbers are in the format: +234 803 456 7890
# Writes the extracted email addresses to a file named emails.txt and the phone numbers to a file named phone_numbers.txt.

# Requirements:
# Use regular expressions to find the email addresses and phone numbers.
# Ensure that the extracted data is saved in separate files, one for emails and one for phone numbers.

# Example:
# Given the following content in reviews.txt:

# Customer feedback:
# - Email: john.doe@example.com
# - Phone: +234 803 456 7890
# - Another contact: jane_smith@workplace.org
# - Alternate phone: +234 701 234 5678

# The script should produce:
# emails.txt containing:
# john.doe@example.com
# jane_smith@workplace.org
# phone_numbers.txt containing:
# +234 803 456 7890 
# +234 701 234 5678

# 	Go here and download the `reviews.txt` file to use.

# Reads the contents of a text file named reviews.txt.
with open("reviews.txt", "r") as f:
    text = f.read()
print(text)

#  Extracting Data

import re
# Extract emails in username@domain.tld format
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2}"
emails = re.findall(pattern, text)
if emails:
    print("Email found:", emails)  # Email found: support@example.com


pattern = r"\+234\s\d{3}\s\d{3}\s\d{4}"
phone_numbers = re.findall(pattern, text)
if phone_numbers:
    print("Phone numers found:", phone_numbers)

with open("emails.txt", "w") as f:
    for email in emails:
        f.write(email + "\n")

with open("phone_numbers.txt", "w") as f:
    for phone_number in phone_numbers:
        f.write(phone_number + "\n")