# ====================ASSIGNMENT=================================

# 1. Print the second and seco nd-to-last items in the list.
# animals = ["dog", "cat", "goat", "cow", "sheep", "horse"]
# print(f"{animals[1]} \n{animals[4]}")
# print(animals[1] + "\n"  + animals[4])
# Expected Output:
# cat
# sheep

# 2. Replace the first and last items with "lion" and "elephant", then print the list.
# animals = ["dog", "cat", "goat", "cow", "sheep", "horse"]
# animals[0] = "lion"
# animals[-1] = "elephant"
# print(animals)
# Expected Output:
# ['lion', 'cat', 'goat', 'cow', 'sheep', 'elephant']


# 3. Add "pig" to the list and then insert "hen" at index 2.
# animals = ["dog", "cat", "goat"]
# animals.append("pig")
# animals.insert(2, "hen")
# print(animals)
# Expected Output:
# ['dog', 'cat', 'hen', 'goat', 'pig']


# 4. Remove "cow" from the list and print the updated list.
# animals = ["dog", "cat", "cow", "goat", "sheep"]
# animals.remove("cow")
# print(animals)
# Expected Output:
# ['dog', 'cat', 'goat', 'sheep']


# 5. Check if "goat" is in the list and print the result.
# animals = ["dog", "cat", "cow", "goat", "sheep"]
# print("goat" in animals)
# Expected Output:
# True


# 6. Combine two lists of foods and print the result.
# list1 = ["rice", "beans"]
# list2 = ["yam", "plantain"]
# print(list1 + list2)
# Expected Output:
# ['rice', 'beans', 'yam', 'plantain']


# 7. Create a list of drinks and check if "water" exists.
# drinks = ["tea", "coffee", "juice", "soda"]
# print("water" in drinks)
# Expected Output:
# False


# 8. Add "water" and "milk" at once to the list.
# drinks = ["tea", "coffee", "juice"]
# drinks.extend(["water", "milk"])
# print(drinks)
# Expected Output:
# ['tea', 'coffee', 'juice', 'water', 'milk']


# 9. Replace "coffee" with "hot chocolate" and print the list.
# drinks = ["tea", "coffee", "juice"]
# drinks[1] = "hot chocolate"
# print(drinks)
# Expected Output:
# ['tea', 'hot chocolate', 'juice']


# 10. Create a list of vehicles, add and remove some items step by step.
# vehicles = ["car", "bike", "bus", "train"]
# Steps:
#    
#   2. Insert "truck" at index 1
# vehicles.insert(1, "truck")
# print(vehicles)
#   3. Remove "bike"
# vehicles.remove("bike")
# print(vehicles)
#   4. Check if "plane" exists
# print("plane" in vehicles)
# Expected Output:
# ['car', 'truck', 'bus', 'train', 'boat']
# False


# 11. Append "Abuja" to the end of the list.
# cities = ["Lagos", "Kano", "Ibadan"]
# cities.append("Abuja")
# print(cities)
# Expected Output:
# ['Lagos', 'Kano', 'Ibadan', 'Abuja']


# 12. Extend the list with another list of cities.
# cities = ["Lagos", "Kano"] 
# more_cities = ["Abuja", "Enugu"]
# print(cities + more_cities)
# Expected Output:
# ['Lagos', 'Kano', 'Abuja', 'Enugu']