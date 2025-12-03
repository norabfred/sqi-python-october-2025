# # Fill in the Line class methods to accept coordinates as a pair of tuples and 
# # return the slope and distance of the line. Look up the formulas for finding the distance and slope of a line.


# class Line:
#     def __init__(self, coor1, coor2): 
#         self.x1, self.y1 = coor1
#         self.x2, self.y2 = coor2
#     def distance(self):
#       return(((self.x2 - self.x1)**2 + (self.y2 - self.y1) **2) ** 0.5) # root 2 of(x2 -x1)**"" + (y2-y1)**2

#     def slope(self):
#       return (self.y2 - self.y1) / (self.x2 - self.x1)


#  EXAMPLE EXECUTION

# coordinatel = (3,2)
# # # coordinate2 = (8,10)

# # # line_1 = Line(coordinatel, coordinate2)

# # # print(line_1.distance())  # 9.433981132056603
# # # print(line_1.slope())  # 1.6

# # # -----------------------------NUMBER 2-----------------------------------------------------
# # #  2.	Fill in the class

# # class Cylinder:
# #     def __init__(self, height=1, radius=1):
# #         self.height = height
# #         self.radius = radius

# #     def volume (self):
# #         return 22/7 * (self.radius **2) * self.height #Volume = PI * r**2 * h

# #     def surface_area(self):
# #         return (2 * 22/7 * (self.radius **2)) + (2 * 22/7 * self.radius * self.height) # = 2 * PI * r**2 + 2 * PI *r * h

# # # EXAMPLE EXECUTION

# # cylinder = Cylinder(2,3)
# # print(cylinder.volume())  # 56.52
# # print(cylinder.surface_area())  # 94.2

# # --------------------------------ACCOUNTANT ASSIGNMENT-----------------------------------------------
# # Scenario: You want to create a bank account that supports deposits and withdrawals.

# # Task: Create a bank account class that has two attributes:
# class BankAccount:
#     def __init__(self, owner: str, balance: int):
#         self.owner = owner
#         self.balance = balance

#     def __str__(self):
#         return f"Accounr owner: {self.owner} \n Account balance: ${self.balance}"
    
#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposit Accepted")

#     def withdrawal(self, amount):
#         if amount > self.balance:
#             print("funds unavailable")
#         else:
#             self.balance -= amount
#             print("Withradwal Accepted")


# # Withdrawals may not exceed the available balance.
# # Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

# # You are not expected to use the input function, just pass in values for the amounts into 
# # the methods directly, no need for loops either.

# # See the next slide for a sample execution of the code you will write.    

# #1. Instantiate the class
# acct1 = BankAccount('Winnie', 100)

# #2. Print the object
# print(acct1)
# # Output:
# # Account owner: Winnie
# # Account balance: $100

# #3. Show the account owner attribute
# print(acct1.owner)  # Winnie

# #4. Show the account balance attribute 
# print(acct1.balance)  # 100

# #5. Make a series of deposits and withdrawals 
# acct1.deposit(50)  # Output: Deposit Accepted

# acct1.withdrawal(15)  # Output: Withdrawal Accepted

# #6. Make a withdrawal that exceeds the available balance 
# acct1.withdrawal(500)  # Output: Funds Unavailable!

# --------------------------------ACCOUNTANT ASSIGNMENT-----------------------------------------------


#---------------------------------SPACE MISSION---------------------------------------------------
# You are building a simple simulation of a space mission. There are different types of spacecraft.

# 1. Create a base class
# Create a class called Spacecraft with:
# Attributes:
# name (string)
# fuel (integer)
class Spacecraft:
    def __init__(self, name: str, fuel: int):
        self.name = name
        self.fuel = fuel
# Methods:
# launch() — prints "Launching {name}!"
# Reduces fuel by 50 units.
# If not enough fuel, print "Not enough fuel to launch."
    def launch(self):
        if self.fuel > 50:
            print(f"launch {self.name}!")
            self.fuel -= 50
        else:
            print("Not enough fuel to launch")

# refuel(amount) — adds amount to fuel.
    def refuel(self, amount):
        self.fuel += amount
        print(f"{self.name} refuelled with {amount} units. Fuel is now {self.fuel}")

# 2. Create subclasses
# CargoShip
# Has an additional attribute: cargo_weight (integer)
# Override launch() — launching consumes extra fuel depending on cargo:
# total fuel reduction = 50 + (cargo_weight * 2)
class CargoShip(Spacecraft):
    def __init__(self, name, fuel, cargo_weight):
        super().__init__(name, fuel)
        self.cargo_weight = cargo_weight
    def launch(self):
        fuel_needed = 50 + (self.cargo_weight * 2)

        if self.fuel >= fuel_needed:
            print(f"Launching {self.name} with cargo!")
            self.fuel -= fuel_needed
        else:
            print("Not enough fuel to launch.")

# PassengerShip
# Has an additional attribute: passenger_count (integer)
# Override launch() — if passenger_count > 100, print "Too many passengers. Cannot launch."
# Otherwise, launch normally (reduce fuel by 50 units)
class PassengerShip(Spacecraft):
    def __init__(self, name, fuel, passenger_count):
        self.passenger_count = passenger_count
        super().__init__(name, fuel)
    def launch(self):
        if self.passenger_count > 100:
            print("Too many passengers. Cannot launch.")
            return
# 3. Handle negative refuel amounts.
        if self.fuel >= 50:
            print(f"Launching {self.name}!")
            self.fuel -= 50
        else:
            print("Not enough fuel to launch.")
# SAMPLE EXECUTION
# Create objects
cargo_ship = CargoShip("Galactic Hauler", 200, 30)
passenger_ship = PassengerShip("Star Voyager", 100, 80)

# Attempt to launch both ships
cargo_ship.launch()
# Output: Launching Galactic Hauler with cargo!
# Fuel after launch: 200 - (50 + 30*2) = 90

passenger_ship.launch()
# Output: Launching Star Voyager!
# Fuel after launch: 100 - 50 = 50

# Refuel both ships
cargo_ship.refuel(50)
# Output: Refueled Galactic Hauler with 50 units. Fuel is now 140.

passenger_ship.refuel(30)
# Output: Refueled Star Voyager with 30 units. Fuel is now 80.

# Launch again after refueling
cargo_ship.launch()
# Output: Launching Galactic Hauler with cargo!
# Fuel after launch: 140 - (50 + 30*2) = 30

passenger_ship.launch()
# Output: Launching Star Voyager!
# Fuel after launch: 80 - 50 = 30

# Try to refuel with invalid amount
cargo_ship.refuel(-10)
# Output: Cannot refuel with negative amount.

# Test PassengerShip with too many passengers
passenger_ship.passenger_count = 120
passenger_ship.launch()
# Output: Too many passengers. Cannot launch.

# Try to launch cargo ship with low fuel
cargo_ship.launch()
# Output: Not enough fuel to launch.





#---------------------------------SPACE MISSION---------------------------------------------------