# # movie_genres = ("comedy", "romance", "thriller", "action", "adventure", "horror", "sci-fi", "anime", "musical")
# # movie_genre_caps = [movie_genre.upper() for movie_genre in movie_genres]
# # print(movie_genre_caps)

# # movie_genres = ("comedy", "romance", "thriller", "action", "adventure", "horror", "sci-fi", "anime", "musical")
# # movie_genre_len = [movie_genre for movie_genre in movie_genres if len(movie_genre) < 6]
# # print(movie_genre_len)

# # all_countries = ["Nigeria", "USA", "Ghana", "UAE", "Canada", "Switzerland", "Japan", "Germany", "Australia", "Togo", "China"]
# # developing_countries =["Nigeria", "Togo", "Ghana"]
# # developed_countries = [country for country in all_countries if country not in developing_countries]
# # print(developed_countries)

# # all_countries = ["Nigeria", "USA", "Ghana", "UAE", "Canada", "Switzerland", "Japan", "Germany", "Australia", "Togo", "China"]
# # country_filtering = [country for country in all_countries if country != "UAE"]
# # print(country_filtering)

# # all_countries = ["Nigeria", "USA", "Ghana", "UAE", "Canada", "Switzerland", "Japan", "Germany", "Australia", "Togo", "China"]
# # start_with_vowel = {country: country.lower().startswith(("a", "e", "i", "o", "u")) for country in all_countries}
# # print(start_with_vowel)

# # multiples_of_3_and_5 = [number for number in range(1, 101) if number % 3 == 0 and number % 5 == 0]
# # print(multiples_of_3_and_5)

# # multiples_of_3_and_5 = [number for number in range(1, 101) if number % 15 == 0]
# # print(multiples_of_3_and_5)


# names = ["John", "Sara", "Mike", "Amanda"]
# contain_a = [name for name in names if ("a") in name]
# print(contain_a)

# animals = ["dog", "cat", "lion", "tiger"]
# last_character = [animal[-1] for animal in animals]
# print(last_character)

# names = ["John", "Sara", "Mike", "Amanda"]
# print(any(name for name in names if ("a") in name))

# greetings = ["HELLO", "world", "pyTHon", "ROCKS"]
# print(all(greeting.isupper() for greeting in greetings))