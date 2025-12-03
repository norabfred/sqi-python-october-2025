# Project Overview:
# Develop an Exam Wizard program in Python that hardcodes a set of at least 5 theory 
# questions and evaluates the student's answers based on the presence of specific keywords or phrases. The program should ask these questions to the user one by one and display the user's score at the end.

# Requirements:
# Hardcode Questions and Keywords:
# Create at least 5 theory questions.
# For each question, determine the essential keywords or phrases that should be included in the ideal answer.
# Assign weights to each keyword based on its importance.
# Question Prompting:
# Prompt the user with each question one by one.
# Allow the user to input their answer for each question.
# Scoring System:
# Evaluate the user's answers based on the presence of the specified keywords..
# Keep track of the user's score.
# Display Results:
# At the end of the quiz, display the user's total score out of the max score e.g. 10/12.
# Sample Question and Evaluation Criteria:
# Question: Explain the process of photosynthesis.

# Ideal Answer: Photosynthesis is a process used by plants and other organisms to convert light energy into chemical energy. It occurs in the chloroplasts of plant cells. The process involves the absorption of light by chlorophyll, the conversion of carbon dioxide and water into glucose and oxygen, and the storage of energy in the form of ATP.

# Keywords and Weights:
# Photosynthesis (2 points)
# Light energy (1 point)
# Chemical energy (1 point)
# Chloroplasts (2 points)
# Chlorophyll (1 point)
# Carbon dioxide (1 point)
# Water (1 point)
# Glucose (1 point)
# Oxygen (1 point)
# ATP (1 point)

# Example of Keyword-Based Marking:
# Student's Answer: Photosynthesis is a process in which plants use sunlight to make 
# food. It happens in the chloroplasts where chlorophyll absorbs light. The plants take in carbon dioxide and water, and produce glucose and oxygen.
# Marked Answer:
# Photosynthesis (2 points)
# Chloroplasts (2 points)
# Chlorophyll (1 point)
# Carbon dioxide (1 point)
# Water (1 point)
# Glucose (1 point)
# Oxygen (1 point)
# Total Score: 9 out of 12 points.


#-----------------------------------ANSWER---------------------------------------------------------
import re

def normalize(text):
    """Lowercase and remove extra punctuation for matching but keep words and spaces."""
    # replace non-alphanumeric (except spaces) with space, collapse spaces
    cleaned = re.sub(r'[^0-9a-zA-Z\s]', ' ', text.lower())
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned

def match_keyword(answer_text, keyword):
    """
    Return True if keyword (single word or multi-word phrase) appears in answer_text.
    Uses simple word-boundary matching for single words and exact substring matching for phrases.
    """
    ans = normalize(answer_text)
    kw = normalize(keyword)
    # Exact phrase check (works for single words and multi-word phrases)
    pattern = r'\b' + re.escape(kw) + r'\b'
    return re.search(pattern, ans) is not None

def run_exam(questions):
    total_score = 0
    max_score = 0
    print("\n--- Exam Wizard: Theory Quiz ---\n")
    for i, q in enumerate(questions, start=1):
        print(f"Question {i}: {q['question']}\n")
        user_ans = input("Your answer: ").strip()
        print("\nEvaluation:")
        q_score = 0
        q_max = 0
        # For each keyword, check presence and award weight
        for kw, weight in q['keywords'].items():
            q_max += weight
            present = match_keyword(user_ans, kw)
            mark = weight if present else 0
            q_score += mark
            status = "FOUND" if present else "missing"
            print(f" - {kw}: {mark}/{weight} ({status})")
        print(f" Score for this question: {q_score}/{q_max}\n")
        total_score += q_score
        max_score += q_max
    print("--- Final Result ---")
    print(f"Total score: {total_score}/{max_score}")
    percentage = (total_score / max_score) * 100 if max_score else 0
    print(f"Percentage: {percentage:.1f}%\n")

if __name__ == "__main__":
    # Hardcoded questions: at least 5. Each has keywords mapped to weights (ints).
    QUESTIONS = [
        {
            "question": "Explain the process of photosynthesis.",
            "keywords": {
                "photosynthesis": 2,
                "light energy": 1,
                "chemical energy": 1,
                "chloroplasts": 2,
                "chlorophyll": 1,
                "carbon dioxide": 1,
                "water": 1,
                "glucose": 1,
                "oxygen": 1,
                "ATP": 1
            }
        },
        {
            "question": "Describe Newton's second law of motion.",
            "keywords": {
                "force": 2,
                "mass": 1,
                "acceleration": 2,
                "F = m a": 2,
                "proportional": 1,
                "net force": 1
            }
        },
        {
            "question": "What is polymorphism in object oriented programming?",
            "keywords": {
                "polymorphism": 2,
                "objects": 1,
                "methods": 1,
                "different forms": 1,
                "inheritance": 1,
                "overriding": 1
            }
        },
        {
            "question": "Explain the structure and function of DNA.",
            "keywords": {
                "deoxyribonucleic acid": 2,
                "double helix": 2,
                "nucleotides": 1,
                "base pairs": 1,
                "adenine": 1,
                "thymine": 1,
                "cytosine": 1,
                "guanine": 1,
                "genetic information": 1
            }
        },
        {
            "question": "Define superbasic concepts of HTTP and REST.",
            "keywords": {
                "http": 2,
                "request": 1,
                "response": 1,
                "stateless": 2,
                "rest": 2,
                "resources": 1,
                "methods": 1
            }
        },
        {
            "question": "What causes tides on Earth?",
            "keywords": {
                "gravity": 2,
                "moon": 2,
                "sun": 1,
                "tidal force": 1,
                "rotation": 1
            }
        }
    ]

    run_exam(QUESTIONS)
#-----------------------------------ANSWER---------------------------------------------------------
