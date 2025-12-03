# Project Overview:
# Develop a simple Computer-Based Testing (CBT) program in Python that hardcodes a set of 
# at least 5 objective questions and their answers. The program should ask these questions 
# to the user one by one and display the user's score at the end.

# Requirements:
# Hardcode Questions and Answers:
# Create at least 5 objective questions (multiple choice or true/false).
# Hardcode these questions and their correct answers in your program.
# Question Prompting:
# Prompt the user with each question one by one.
# Allow the user to input their answer for each question.
# Scoring System:
# Compare the user's answers with the correct answers.
# Keep track of the user's score.
# Display Results:
# At the end of the quiz, display the user's total score.
# Sample Questions:
# What is 2 + 2?
# a) 3
# b) 4
# c) 5
# d) 6
# What color is the sky on a clear day?
# a) Red
# b) Blue
# c) Green
# d) Yellow
# How many legs does a spider have?
# a) 6
# b) 7
# c) 8
# d) 9
# What sound does a cow make?
# a) Meow
# b) Bark
# c) Moo
# d) Quack
# What is the opposite of 'hot'?
# a) Warm
# b) Cold
# c) Cool
# d) Boiling
# Sample Execution:

# 1. What is 2 + 2?
# a) 3
# b) 4
# c) 5
# d) 6

# Enter an option from a to d: b

# 2. What color is the sky on a clear day?
# a) Red
# b) Blue
# c) Green
# d) Yellow

# Enter an option from a to d: b

# 3. How many legs does a spider have?
# a) 6
# b) 7
# c) 8
# d) 9

# Enter an option from a to d: c

# Sample Execution Cont’d:

# 4. What sound does a cow make?
# a) Meow
# b) Bark
# c) Moo
# d) Quack

# Enter an option from a to d: c

# 5. What is the opposite of 'hot'?
# a) Warm
# b) Cold
# c) Cool
# d) Boiling

# Enter an option from a to d: b
# At the end of the CBT exam, you scored 5 points.



#--------------------------------------ANSWER--------------------------------------------------------
questions = [
        {
            "q": "What is 2 + 2?",
            "options": {"a": "3", "b": "4", "c": "5", "d": "6"},
            "answer": "b"
        },
        {
            "q": "What color is the sky on a clear day?",
            "options": {"a": "Red", "b": "Blue", "c": "Green", "d": "Yellow"},
            "answer": "b"
        },
        {
            "q": "How many legs does a spider have?",
            "options": {"a": "6", "b": "7", "c": "8", "d": "9"},
            "answer": "c"
        },
        {
            "q": "What sound does a cow make?",
            "options": {"a": "Meow", "b": "Bark", "c": "Moo", "d": "Quack"},
            "answer": "c"
        },
        {
            "q": "What is the opposite of 'hot'?",
            "options": {"a": "Warm", "b": "Cold", "c": "Cool", "d": "Boiling"},
            "answer": "b"
        },
        {
            "q": "Which planet is known as the Red Planet?",
            "options": {"a": "Venus", "b": "Mars", "c": "Jupiter", "d": "Saturn"},
            "answer": "b"
        }
    ]
def run_cbt():

    print("Welcome to the simple CBT quiz!\nEnter an option from a to d for each question.\n")
def asked_question(quest: dict[str, str]):
        print(quest["q"])
        for key, text in quest["options"].items():
            print(f"{key} {text}")
        while True:
            response = input("Enter your answer(a/b/c/d): ").strip().lower()
            if response in ["a", "b", "c", "d"]:
                break
            print("Invalid entry")

        if response == quest["answer"]:
            return True
        else:
            return False
        
score = 0
total = len(questions)

for quest in questions:
    if asked_question(quest):
        score +=1

    
       
print(f"At the end of the CBT exam, you scored {score} out of {total} points.")

# if __name__ == "__main__":
#     run_cbt()
    # run_cbt() 
#--------------------------------------ANSWER--------------------------------------------------------
