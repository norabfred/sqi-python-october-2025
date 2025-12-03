# ...............................FIRST ASSIGNMENT.........................................
# 1. Create a dictionary called `student` with keys "name", "age", and "grade", and 
# corresponding values "John", 20, and "A". Access and print the value of "name".
print("\n\nQuestion 1")
student = {"name": "John", "age": 20, "grade": "A"}
print(student.get("name"))

# 2. Create a dictionary called `product` with keys "name", "price", and "stock", and 
# corresponding values "Laptop", 999.99, and 50. Change the value of "price" to 899.99.
print("\n\nQuestion 2")
product = {"name": "Laptop", "price": 999.99, "stock": 50}
product["price"] = 899.99
print(product)

# 3. Create a dictionary called `employee` with keys "name" and "position", and corresponding values "Alice" and "Manager". Add a new key "salary" with the value 50000.
print("\n\nQuestion 3")
employee = {"name": "Alice", "position": "Manager"}
employee["Salary"] = 50000
print(employee)

# 4. Create a dictionary called `inventory` with keys "apple", "banana", and "orange", and values 10, 5, and 8 respectively. Remove the key "banana".
print("\n\nQuestion 4")
inventory = {"apple": 10, "banana": 5,"orange": 8}
del inventory["banana"]
print(inventory)

# 5. Create a dictionary called person with keys "name", "age", and "city", and corresponding values "Bob", 25, and "New York". Use the copy() method to make a copy of the dictionary and call it person_copy.
print("\n\nQuestion 5")
person = {"name": "Bob", "age": 25, "city": "New York"}
print(id(person))
person_copy = person.copy()
print(id(person_copy))

# 6. Create a nested dictionary called `family` with keys "child1", "child2", and "child3", each containing a dictionary with keys "name" and "age" with appropriate values. Access and print the age of "child2".
print("\n\nQuestion 6")
family = {
"child1": {"name": "Labake", "age": 32},
"child2": {"name": "Busola", "age": 34},
"child3": {"name": "Blessing", "age": 33}
}
print(family["child2"]["age"])

# 7. Create a dictionary called `car` with keys "brand", "model", and "year", and corresponding values "Toyota", "Corolla", and 2020. Access and print the value of "model".
print("\n\nQuestion 7")
car = {
  "barand": "Toyota", "model": "Corolla", "year": 2020
}
print(car.get("model"))
# print(car["model"])

# 8. Create a dictionary called `settings` with keys "volume", "brightness", and "language", and corresponding values 50, 75, and "English". Change the "language" to "Spanish".
print("\n\nQuestion 8")
settings = {"volume": 50, "brightness": 75, "language": "English"}
print(settings)
settings["language"] = "Spanish"
print(settings)

# 9. Create a dictionary called `scores` with keys "math", "science", and "english", and corresponding values 90, 85, and 88. Remove the key "science".
print("\n\nQuestion 9")
scores = {
  "math": 90, "science": 85, "english": 88
}
scores.pop("science")
print(scores)

# 10. Create a dictionary called `menu` with keys "starter", "main_course", and "dessert", and corresponding values "Soup", "Steak", and "Ice Cream". Check if the key "appetizer" is present in the dictionary.
print("\n\nQuestion 10")
menu = {"starter": "Soup", "main_course": "Steak", "dessert": "Ice Cream"}
print("appetizer" in menu)

# 11. Create a dictionary called `config` with keys "theme", "language", and "timezone", and corresponding values "dark", "English", and "UTC". Clear the dictionary.
print("\n\nQuestion 11")
config ={"themes": "dark", "language": "English", "timezone": "UTC"}
config.clear()
print(config)

# 12. Create a dictionary called `phone_book` with keys "Alice", "Bob", and 
# "Charlie", and corresponding phone numbers as values. Print the number of items in the dictionary.
print("\n\nQuestion 12")
phone_book = {"Alice": "07067890034", "Bob": "0803211065", "Charlie": "08122889012"}
print(len(phone_book))
      
# 13. Create a dictionary called `grades` with keys "math", "science", and "history", 
# and corresponding values "A", "B", and "C". Get a LIST of all the keys in the 
# dictionary.
print("\n\nQuestion 13")
grades = {
  "math": "A", "science": "B", "history": "C"
}
print(grades.keys())

# 14.	Create a dictionary called `employee` with keys "name", "position", and 
# "salary", and corresponding values "David", "Engineer", and 70000. Get a LIST of all the values in the dictionary.
print("\n\nQuestion 14")
employee = {"name": "David", "position": "Engineer", "salary": 70000}
print(employee.values())

# 15. Create a dictionary called `game` with keys "title", "genre", and "rating", and 
# corresponding values "Minecraft", "Sandbox", and 4.5. Get a LIST of all 
# key-value pairs in the dictionary.
print("\n\nQuestion 15")
game = {"title": "Minecraft", "genre": "Sandbox", "rating": 4.5}
print(game.items())

#........................................SECOND ASSIGNMENT.............................................
# ===============================
# Nested Dictionary Modification Exercises
# ===============================

# Q1. Given this dictionary, change the "math" score to 95.
print("\n\nsecond assignmentt")
print("\n\nQuestion 1")
student = {
    "name": "Alice",
    "scores": {"math": 80, "english": 85}
}
student["scores"]["math"] = 95
print(student)
# Expected Output:
# {'name': 'Alice', 'scores': {'math': 95, 'english': 85}}


# Q2. Add a new subject "science" with score 90 inside "scores".
print("\n\nQuestion 2")
student = {
    "name": "Alice",
    "scores": {"math": 80, "english": 85}
}
student["scores"]["science"] = 90
print(student)
# Expected Output:
# {'name': 'Alice', 'scores': {'math': 80, 'english': 85, 'science': 90}}

# Q3. Change the author's name of "Python 101" to "Mike".
print("\n\nQuestion 3")
library = {
    "Python 101": {"author": "Tom", "year": 2020},
    "Data Science": {"author": "Jane", "year": 2021}
}
library["Python 101"]["author"] = "Mike"
print(library)
# Expected Output:
# {'Python 101': {'author': 'Mike', 'year': 2020}, 'Data Science': {'author': 'Jane', 'year': 2021}}


# Q4. Add a new key "publisher" = "O'Reilly" to "Data Science".
print("\n\nQuestion 4")
library = {
    "Python 101": {"author": "Tom", "year": 2020},
    "Data Science": {"author": "Jane", "year": 2021}
}
library["Data Science"]["publisher"] = "O'Reilly"
print(library)
# Expected Output:
# {'Python 101': {'author': 'Tom', 'year': 2020}, 'Data Science': {'author': 'Jane', 'year': 2021, 'publisher': "O'Reilly"}}

# Q5. In this dictionary, add a new phone number "work": "555-999" for Alice.
print("\n\nQuestion 5")
contacts = {
    "Alice": {"home": "555-123", "mobile": "555-456"},
    "Bob": {"home": "555-789"}
}
contacts["Alice"]["work"] = "555-999"
print(contacts)
# Expected Output:
# {'Alice': {'home': '555-123', 'mobile': '555-456', 'work': '555-999'}, 'Bob': {'home': '555-789'}}


# Q6. Change Bob’s "home" number to "555-000".
print("\n\nQuestion 6")
contacts = {
    "Alice": {"home": "555-123", "mobile": "555-456"},
    "Bob": {"home": "555-789"}
}
contacts["Bob"]["home"] = "555-000"
print(contacts)
# Expected Output:
# {'Alice': {'home': '555-123', 'mobile': '555-456'}, 'Bob': {'home': '555-000'}}


# Q7. Add a new student {"name": "Eve", "scores": {"math": 88, "english": 92}}
# into the list of students.
print("\n\nQuestion 7")
students = [
    {"name": "Alice", "scores": {"math": 80, "english": 85}},
    {"name": "Bob", "scores": {"math": 75, "english": 70}}
]
students.append({"name": "Eve", "scores": {"math": 88, "english": 92}})
print(students)
# Expected Output:
# [{'name': 'Alice', 'scores': {'math': 80, 'english': 85}},
#  {'name': 'Bob', 'scores': {'math': 75, 'english': 70}},
#  {'name': 'Eve', 'scores': {'math': 88, 'english': 92}}]


# Q8. Change Bob's english score from 70 to 78.
print("\n\nQuestion 8")
students = [
    {"name": "Alice", "scores": {"math": 80, "english": 85}},
    {"name": "Bob", "scores": {"math": 75, "english": 70}}
]
students[1]["scores"]["english"]= 78
print(students)
# Expected Output:
# [{'name': 'Alice', 'scores': {'math': 80, 'english': 85}},
#  {'name': 'Bob', 'scores': {'math': 75, 'english': 78}}]


# Q9. Add a new dictionary {"year": 2022, "semester": "Spring"} 
# inside Alice’s record under a new key "enrollment".
print("\n\nQuestion 9")
students = [
    {"name": "Alice", "scores": {"math": 80, "english": 85}},
    {"name": "Bob", "scores": {"math": 75, "english": 78}}
]
students[0]["enrollment"] = {"year": 2022, "semester": "Spring"} 
print(students)
# Expected Output:
# [{'name': 'Alice', 'scores': {'math': 80, 'english': 85}, 'enrollment': {'year': 2022, 'semester': 'Spring'}},
#  {'name': 'Bob', 'scores': {'math': 75, 'english': 78}}]

# Q10. In this shop cart, add a new product "Notebook" with price 200.
print("\n\nQuestion 10")
cart = {
    "items": [
        {"name": "Pen", "price": 10},
        {"name": "Book", "price": 50}
    ],
    "owner": "Alice"
}
cart["items"].append({"name": "Notebook", "price": 200})
print(cart)
# Expected Output:
# {'items': [{'name': 'Pen', 'price': 10}, {'name': 'Book', 'price': 50}, {'name': 'Notebook', 'price': 200}],
#  'owner': 'Alice'}











