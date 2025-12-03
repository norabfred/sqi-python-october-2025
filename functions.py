# def my_name():
#     print("Blessing")

# my_name()

# def double_num(num):
#     print(num * 2)

# double_num(5)

# def introduction(name):
#     print(f"I am {name}")
# introduction("Blessing")

# def raise_to_power(base, exponent):
#     print(base ** exponent)
# raise_to_power(2, 3)

# def change_to_lower(word):
#     return word.lower()
# print(change_to_lower("RICE"))

 
# def upper_everyone(names: list[str]):
#     upper = [name.upper() for name in names]
#     print(upper)
# upper_everyone(["Blessing", "Feyi", "Ife", "Francis", "Towi"]) 


# def starts_with_m(word):
#     has_m = word.lower().startswith("m")
#     print(has_m)
# starts_with_m("Maddie")

# def is_even(num):
#     return num % 2 == 0 
    
# print(is_even(6))


def is_alliteration(words: str):
    two_word_string = words.lower().split()
    return two_word_string[0][0] == two_word_string[1][0]
print(is_alliteration("Levelheaded llama"))
print(is_alliteration("Happy llama"))