# # class Car:
# #     def __init__(self, color: str, brand: str, model: str, year_manufactured: int, engine: str, no_of_doors: int):
# #         self.color = color
# #         self.brand = brand
# #         self.model = model
# #         self.year_manufactured = year_manufactured
# #         self.engine = engine
# #         self.no_of_doors = no_of_doors
    
# #     def move(self):
# #         return f"The {self.color} {self.brand} {self.model} is moving"
# #     def reverse(self):
# #         return f"The {self.color} {self.brand} {self.model} is reversing"
# #     def honk(self):
# #         return f"The {self.color} {self.brand} {self.model} with {self.no_of_doors} doors is honking"
# # car1 = Car("black", "Benz", "GLE 500", 2024, "v-6", 4)
# # car2 = Car("white", "toyota", "carina E", 2008, "v-6", 2)
# # car3 = Car("red", "hunda", "pilot", 2025, "v-4", 4)
# # print(car1.move())
# # print(car2.reverse())
# # print(car3.honk())

# class Movie:
#     def __init__(self, title: str, produced_by: str, directed_by: str, year_relaease: int, no_of_cast: int, genre: str):
#         self.title = title
#         self.produced_by =produced_by
#         self.directed_by = directed_by
#         self.year_released = year_relaease
#         self.no_of_cast = no_of_cast
#         self.genre = genre

#     def rating(self):
#         return f"The movie titled {self.title} directed by {self.directed_by} was rated among the top 10 movies on netflix"
# movie1 = Movie("The hollow", "Tyler Perry", "Frederick Blessing", 2025, 75, "action")
# print(movie1.title)
# movie1.title = "walking Dead"
# print(movie1.title)
# print(movie1.rating())


# # OOP - Object Oriented Programming

# # Functional & Modular Programming

# # OOP - Object and Class



# # class BankAccount:
# #     # magic dunder method
# #     def __init__(self, bank_name: str, account_number: str, account_owner: str, balance: int, is_savings: bool):
# #         self.bank_name = bank_name
# #         self.account_no = account_number
# #         self.account_owner = account_owner
# #         self.balance = balance
# #         self.is_savings = is_savings
# #         # print("Something")
# #         # print(is_savings)


# #     def check_account_details(self):
# #         return f"{self.account_owner}'s {self.bank_name} account. Account number - {self.account_no}."
    


# # # print(str(4))

# # # int()

# # ife_bank_acct = BankAccount("GTBank", "0318497832", "Ife Omole", 3_200_000, False)
# # sarah_bank_acct = BankAccount("Access Bank", "0788419919", "Sarah Omoseeke", 4_000_900, True)

# # # print(BankAccount("Access Bank", "0788419919", "Sarah Omoseeke", 4_000_900, True))

# # print(ife_bank_acct.account_no)
# # print(ife_bank_acct.bank_name)
# # print(ife_bank_acct.balance)
# # print(ife_bank_acct.check_account_details())
# # print(sarah_bank_acct.check_account_details())

# # def greet():
# #     return "Hello"


# # print(greet())


# # class Person:
# #     def __init__(self, name, age, height, weight, is_male: bool, complexion, occupation):
# #         self.name = name
# #         self.age = age
# #         self.height = height
# #         self.weight = weight
# #         self.is_male = is_male
# #         self.complexion = complexion
# #         self.occupation = occupation


# #     def introduce_yourself(self):
# #         gender = "Male" if self.is_male else "Female"  # ternary operator
# #         return f"My name is {self.name}. I am a/an {self.occupation}. I am a {gender}."
        

# # towi = Person("Towi Iji", 30, 1.67, 56, False, "caramel", "student")

# # print(towi.weight)
# # print(towi.occupation)

# # towi.occupation = "Software Engineer"

# # print(towi.occupation)

# # print(towi.introduce_yourself())






# # is_male = True


# # if is_male:
# #     gender = "Male"
# # else:
# #     gender = "Female"



# # gender = "Male" if is_male else "Female"

# # # Create a Car class that has the following attributes:
# # # - color: str
# # # - brand: str
# # # - model: str
# # # - year_manufactured: int
# # # - engine: str
# # # no_of_doors: int

# # # Create 3 objects out of the class
# # # The objects created out of the class should be able to move, reverse, honk


# #-----------------------CLASS WORK-------------------------------------
# class CartItem:
#     def __init__(self, name: str, price: int, quantity: int):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

# class Cart:
#     def __init__(self, cartItems):
#         self.cartItems = cartItems
#     def total_cart(self):
#         return sum(cart_item.price * cart_item.quantity for cart_item in self.cartItems)
# Cart_Item1 = CartItem("eggs", 250, 4)
# Cart_Item2 = CartItem("bread", 1200, 6)

# Cart = Cart([Cart_Item1, Cart_Item2])
# print(Cart.total_cart())

# class Vehicle:
#     def __init__(self, name):
#         self.name = name

#     def describe(self):
#         return f"Vehicle: {self.name}"

# vehicle = Vehicle(name="Bicycle")
# print(vehicle.describe())

# class Car(Vehicle):
#     def __init__(self, name, no_of_doors):
#         self.no_of_doors = no_of_doors
#         super().__init__(name)
#     def describe(self):
#         return f"Car: {self.name} with {self.no_of_doors} doors"
# car = Car(name="Toyota", no_of_doors=4)
# print(car.describe())
# #-----------------------CLASS WORK-------------------------------------


