# ---------------------------------ARITHMETIC OPERATORS-----------------------------------

# print(6 + 7)
# print(6 + 7 + 2)

# operands - values or variables being operated on
# operator - this is the symbol of the operation


# polymorphic - many shape/form


# num1 = 56
# num2 = 91
# print(num1 + num2)

# print(7 + num1)


# print(34 - 12)
# print(12 - 34)


# first_num = 45
# second_num = 2
# print(first_num * second_num)
# print(first_num ** second_num)
# print(2 ** 3)



# / - float division
# // - floor division
# % - modulus op


# print(5 / 3)
# print(0.1 + 0.2)

# from decimal import Decimal

# print(Decimal("0.1"))
# print(Decimal("0.2"))
# print(Decimal("0.1") + Decimal("0.2"))


# print(Decimal("14") / 2)
# print(14 / 2)

# print(14 / 0)


# text = "hello"
# print(text[100])


# print(9 / 4)  # 2.25
# print(9 // 4) # 2
# print(13 // 3)  # 4
# print(13 % 3)  # 1
# print(7 // 2)  # 3


# no_of_balls = 100
# no_of_boxes = 7
# print(no_of_balls // no_of_boxes)
# print(no_of_balls % no_of_boxes)


# no_of_minutes = 670
# # "11 hours, 10 minutes"

# print(f"{no_of_minutes // 60} hours, {no_of_minutes % 60} minutes")



# num = 8
# num = 7
# print(num % 2 == 0)

# Ask the user for a number
# Print True is the number is a multiple of 5, otherwise, print False

# number = int(input("Enter a number: "))
# print(number % 5 == 0)

# ---------------------------------ARITHMETIC OPERATORS-----------------------------------


# ---------------------------------ARITHMETIC OPERATORS-----------------------------------

# print(6 + 7)
# print(6 + 7 + 2)

# operands - values or variables being operated on
# operator - this is the symbol of the operation


# polymorphic - many shape/form


# num1 = 56
# num2 = 91
# print(num1 + num2)

# print(7 + num1)


# print(34 - 12)
# print(12 - 34)


# first_num = 45
# second_num = 2
# print(first_num * second_num)
# print(first_num ** second_num)
# print(2 ** 3)



# / - float division
# // - floor division
# % - modulus op


# print(5 / 3)
# print(0.1 + 0.2)

# from decimal import Decimal

# print(Decimal("0.1"))
# print(Decimal("0.2"))
# print(Decimal("0.1") + Decimal("0.2"))


# print(Decimal("14") / 2)
# print(14 / 2)

# print(14 / 0)


# text = "hello"
# print(text[100])


# print(9 / 4)  # 2.25
# print(9 // 4) # 2
# print(13 // 3)  # 4
# print(13 % 3)  # 1
# print(7 // 2)  # 3


# no_of_balls = 100
# no_of_boxes = 7
# print(no_of_balls // no_of_boxes)
# print(no_of_balls % no_of_boxes)


# no_of_minutes = 670
# # "11 hours, 10 minutes"

# print(f"{no_of_minutes // 60} hours, {no_of_minutes % 60} minutes")



# num = 8
# num = 7
# print(num % 2 == 0)

# Ask the user for a number
# Print True is the number is a multiple of 5, otherwise, print False

# number = int(input("Enter a number: "))
# print(number % 5 == 0)

# ---------------------------------ARITHMETIC OPERATORS-----------------------------------


# ---------------------------------ASSIGNMENT OPERATORS-----------------------------------

# no_of_apples = 10

# # no_of_apples += 4
# # print(no_of_apples)
# no_of_apples = no_of_apples + 4
# print(no_of_apples)


# total_distance = 0
# distance_from_home_to_school = 4
# total_distance += distance_from_home_to_school
# print(total_distance)
# total_distance = total_distance + distance_from_home_to_school
# print(total_distance)

# distance_from_school_to_church = 5


# i = 0
# i += 1


# balance = 7000
# amount_to_withdraw = 300
# balance -= amount_to_withdraw
# print(balance)


# num1 = 8
# num1 *= 2
# # num1 = num1 * 2
# print(num1)



# num1 = 76
# num2 = 3
# num1 /= num2
# print(num1)
# num1 = num1 / num2
# print(num1)
# ---------------------------------ASSIGNMENT OPERATORS-----------------------------------


# ---------------------------------COMPARISON OPERATORS-----------------------------------

# first_num = 4
# second_num = 4
# print(first_num == second_num)
# print(first_num < second_num)
# print(second_num < first_num)
# print(second_num <= first_num)

# first_num = 4
# second_num = 4.0
# print(first_num != second_num)
# print(first_num == second_num)

# ---------------------------------COMPARISON OPERATORS-----------------------------------

# ---------------------------------LOGICAL OPERATORS-----------------------------------

# is_tall = True
# is_male = False

# print(is_tall and is_male)
# print(is_tall or is_male)


# print(5 < 7 or 3 > 4)

# print(6 != 7 and 5 > 12)
# print(6 != 7 or 5 > 12)

# is_tall = True
# is_male = False
# is_young = False

# print(is_tall and is_male and is_young)  # False
# print(is_tall or is_male or is_young)  # True
# print(is_tall and is_male or is_young)  # False
# print(is_tall or is_male and is_young)  # True


# print(not(is_tall))

# print(not(is_young))

# print(7 != 7)
# print(not(7 != 7))

# is_tall = True
# is_male = False
# is_young = False

# print(is_tall or not(is_male) and is_young)  # 
# print(not(is_tall or is_male and is_young))  # False
# ---------------------------------LOGICAL OPERATORS-----------------------------------


# ---------------------------------IDENTITY OPERATORS-----------------------------------

# name1 = "Francis"
# name2 = "Francis"
# name3 = "Feyi"
# print(name1 == name2)
# print(name1 == name3)
# print(name1 is name2)


# print(2 is 2)
# print(-10 is -10)

# interning

# my_list = ["Feyi", "Sarah", "Blessing", "Ife", "Francis"]
# my_list2 = my_list  # reference, not copy
# print(my_list)
# print(my_list2)

# my_list.append("Winnie")
# my_list.remove("Sarah")
# print(my_list)
# print(my_list2)
# print(id(my_list))
# print(id(my_list2))
# print(id(my_list) == id(my_list2))

# print(my_list is my_list2)


# my_list = ["Feyi", "Sarah", "Blessing", "Ife", "Francis"]
# my_list2 = my_list.copy()  # reference, not copy
# print("my_list:", my_list)
# print("my_list2:", my_list2)

# my_list.append("Winnie")
# # my_list.remove("Sarah")
# print("my_list:", my_list)
# print("my_list2:", my_list2)


# print(id(my_list))
# print(id(my_list2))
# print(my_list is my_list2)
# print(id(my_list) == id(my_list2))
# print(my_list == my_list2)

# import copy

# names = [[12, "Blessing"], [20, "Feyi"], [35, "Ife"], [3, "Francis"], [6, "Sarah"]]
# names2 = names.copy()
# # names2 = copy.copy(names)
# # names2 = copy.deepcopy(names)
# print(id(names))
# print(id(names2))
# print(names is names2)
# print(id(names[0]))
# print(id(names2[0]))
# print(names[0] is names2[0])
# names[2][1] = "Victor"
# print(names)
# print(names2)

# python gotcha 

# colors = ["red", "green", "blue"]
# colors2 = colors
# print(colors is colors2)  # True
# print(colors is not colors2)  # False
# print(not(colors is colors2))  # False

# num1 = 500
# num2 = 500
# print(num1 is num2)
# ---------------------------------IDENTITY OPERATORS-----------------------------------



# ---------------------------------MEMBERSHIP OPERATORS-----------------------------------

# my_list = ["Feyi", "Sarah", "Blessing", "Ife", "Francis"]
# print("Ife" in my_list)
# print("ife" in my_list)
# print("Winnie" in my_list)
# print("Winnie" not in my_list)


# language = "Python"
# print("y" in language)

# print(1 in 12)

# ---------------------------------MEMBERSHIP OPERATORS-----------------------------------



# print(not (5 == 3 or 3 > 1))
# print(8 / (4 * 2))
# print(8 / 4 * 2)
# print((8 / 4) * 2)
# print(8 * 4 / 2)


