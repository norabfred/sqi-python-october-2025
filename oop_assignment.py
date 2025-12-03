# # -----------------------------------------ASSIGNMENT-----------------------------------------------
# # 1. Create a class called Book with the following attributes:
# #    - title
# #    - author
# #    - genre
# #    - page_count
# #    - year_published
# #
# #    The class should have a method called short_description() that returns:
# #    "{title} by {author} ({year_published}), {genre}, {page_count} pages."
# #
# #    After defining the class, create 3 different Book objects with different values.

# class Book():
#     def __init__(self, title: str, author: str, genre: str, page_count: int, year_published):
#         self.title = title
#         self.author = author
#         self.genre = genre
#         self.page_count = page_count
#         self.year_published = year_published
    
#     def short_description(self):
#         return f"{self.title} by {self.author} published in {self.year_published} is a/an {self.genre} book with {self.page_count} number of pages"
# book1 = Book("Half of a yellow sun", "Chimamanda Adiche", "drama", 125, 2006)   
# book2 = Book("Alice's Adventures in Wonderland", "Lewis Carroll", "adventure", 178, 2010)   
# book3 = Book("Invisible man", "Ralph Ellison", "Ralph Ellison", 205, 2009)   
# print(book1.short_description())
# print(book2.short_description())
# print(book3.short_description())
# # ---------------------------------------------------------------------------------------------------


# # -----------------------------------------ASSIGNMENT-----------------------------------------------
# # 2. Create a class called Car with the following attributes:
# #    - brand
# #    - model
# #    - year
# #    - horsepower
# #    - fuel_type
# #
# #    The class should have a method called car_info() that returns:
# #    "This is a {year} {brand} {model} with {horsepower} HP running on {fuel_type}."
# #
# #    After defining the class, create 3 different Car objects with different values.
# class Car():
#     def __init__(self, brand: str, model: str, year: int, horsepower: str, fuel_type: str):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.horsepower = horsepower
#         self.fuel_type = fuel_type
#     def car_info(self):
#         return f"This is a {self.year} {self.brand} {self.model} with {self.horsepower} HP running on {self.fuel_type}" 
# car1 = Car("Toyota", "Corolla", 2023, 139, "petrol")    
# car2 = Car("BMW", "M3", 2021, 473, "petrol")    
# car3 = Car("Tesla", "Model 3", 2023, 283, "electric")    
# print(car1.car_info())
# print(car2.car_info())
# print(car3.car_info())
#------------------------------------------------------------------------------------------------------
# 3. Create a class called Student with the following attributes:
#    - name
#    - age
#    - grades (a list of integers)
#
#    The class should have two methods:
#    - average_grade(): returns the average of all grades
#    - is_passing(): returns True if the average grade is >= 50, otherwise False
#
#    After defining the class, create 2 different Student objects with different values.
 
# Example usage:
# s1 = Student("Alice", 20, [60, 75, 80, 90])
# # s2 = Student("Bob", 19, [30, 40, 20, 45])

# # print(s1.name, "average:", s1.average_grade(), "passing:", s1.is_passing())
# # print(s2.name, "average:", s2.average_grade(), "passing:", s2.is_passing())

# # Expected Output:
# # Alice average: 76.25 passing: True
# # Bob average: 33.75 passing: False


# class Student:
#     def __init__(self, name: str, age: int, grades: int):
#         self.name = name
#         self.age = age
#         self.grades = grades
#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)
#     def is_passing(self):
#         return self.average_grade() >= 50
# s1 = Student("Alice", 20, [60, 75, 80, 90])
# s2 = Student("Bob", 19, [30, 40, 20, 45])

# print(s1.name, "average:", s1.average_grade(), "passing:", s1.is_passing())
# print(s2.name, "average:", s2.average_grade(), "passing:", s2.is_passing())

# ----------------------------------------------------------------------------------------------------------
# # 4. Create a class called Playlist with the following attributes:
#    - name
#    - songs (a list of strings)
#
#    The class should have three methods:
# #    - add_song(song): adds a new song title to the playlist
# #    - total_songs(): returns the total number of songs
# #    - show_songs(): returns all song titles as a comma-separated string
# #
# #    After defining the class, create a Playlist and add a few songs.

# # Example usage:
# # pl = Playlist("Workout Jams", ["Eye of the Tiger", "Stronger"])
# # pl.add_song("Lose Yourself")
# # pl.add_song("Can't Hold Us")

# # print(pl.name, "has", pl.total_songs(), "songs")
# # print("Songs:", pl.show_songs())

# # Expected Output:
# # Workout Jams has 4 songs
# # Songs: Eye of the Tiger, Stronger, Lose Yourself, Can't Hold Us
# # class Playlist():
# #     def __init__(self, name: str, songs: list):
# #         self.name = name
# #         self.songs = songs
# #     def add_song(self, song):
# #         self.songs.append(song)
# #     def total_songs(self):
# #         return len(self.songs)
# #     def show_songs(self):
# #         return (", ".join(self.songs))
# # pl = Playlist("Workout Jams", ["Eye of the Tiger", "Stronger"])
# # pl.add_song("Lose Yourself")
# # pl.add_song("Can't Hold Us")

# # print(pl.name, "has", pl.total_songs(), "songs")
# # print("Songs:", pl.show_songs())
# # --------------------------------------------------------------------------------------------------------
# # 5. Create a class called ShoppingCart with the following attributes:
# #    - owner
# #    - items (a dictionary where keys are item names and values are prices)
# #
# #    The class should have three methods:
# #    - add_item(item, price): adds the item with its price
# #    - total_cost(): returns the sum of all prices
# #    - most_expensive(): returns the item with the highest price
# #
# #    After defining the class, create a ShoppingCart and add multiple items.

# # Example usage:
# # cart = ShoppingCart("Alice", {})
# # cart.add_item("Laptop", 1200)
# # cart.add_item("Mouse", 25)
# # cart.add_item("Keyboard", 100)
# # cart.add_item("Monitor", 300)

# # print("Total cost:", cart.total_cost())
# # print("Most expensive item:", cart.most_expensive())

# # Expected Output:
# # Total cost: 1625
# # Most expensive item: Laptop

# class ShoppingCart():
#     def __init__(self, owner: str, items: dict):
#         self.owner = owner
#         self.items = items
#     def add_item(self, item, price):
#         self.items[item] = price
#     def total_cost(self):
#         return sum(self.items.values())
#     def most_expensive(self):
#         return max(self.items, key=self.items.get)
# cart = ShoppingCart("Alice", {})
# cart.add_item("Laptop", 1200)
# cart.add_item("Mouse", 25)
# cart.add_item("Keyboard", 100)
# cart.add_item("Monitor", 300)

# print("Total cost:", cart.total_cost())
# print("Most expensive item:", cart.most_expensive())
# ---------------------------------------------------------------------------------------------------

#------------------------------ASSIGNMENT GIVEN ON 19TH NOV 2025---------------------------------
# warehouse = Warehouse({
#     "laptop": 10,
#     "phone": 25,
#     "headphones": 50
# })
# order1 = Order([
#     OrderItem("laptop", 2),
#     OrderItem("phone", 5)
# ])

# order2 = Order([
#     OrderItem("laptop", 9), 
#     OrderItem("headphones", 2)
# ])

# print(warehouse.place_order(order1))
# # -> True

# print(warehouse.inventory)
# # -> {'laptop': 8, 'phone': 20, 'headphones': 50}

# print(warehouse.place_order(order2))
# # -> False

# print(warehouse.inventory)
# # -> {'laptop': 8, 'phone': 20, 'headphones': 50}


class OrderItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class Order:
    def __init__(self, items):
        # items is a list of OrderItem objects
        self.items = items


class Warehouse:
    def __init__(self, inventory):
        # inventory is a dictionary {item_name: quantity}
        self.inventory = inventory

    def place_order(self, order):
        """Try to place an order. Return True if successful, else False."""
        for item in order.items:
            if item.name not in self.inventory or self.inventory[item.name] < item.quantity:
                return False
        for item in order.items:
            self.inventory[item.name] -= item.quantity

        return True

warehouse = Warehouse({
    "laptop": 10,
    "phone": 25,
    "headphones": 50
})

order1 = Order([
    OrderItem("laptop", 2),
    OrderItem("phone", 5)
])

order2 = Order([
    OrderItem("laptop", 9),
    OrderItem("headphones", 2)
])

print(warehouse.place_order(order1))   # -> True
print(warehouse.inventory)             # -> {'laptop': 8, 'phone': 20, 'headphones': 50}

print(warehouse.place_order(order2))   # -> False
print(warehouse.inventory)             # -> {'laptop': 8, 'phone': 20, 'headphones': 50}

#------------------------------ASSIGNMENT GIVEN ON 19TH NOV 2025---------------------------------
