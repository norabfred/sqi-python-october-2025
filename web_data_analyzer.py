# Objective: Create a Python project that reads data from a file, processes it using a custom module, and fetches 
# additional information from the web using a third-party library. Organize your code into packages and modules to 
# structure the project effectively.

# Instructions:
# Create a Package and Module:
# Create a package named data_processing.
# Inside data_processing, create two modules:
# file_reader.py for reading and processing data from a file.
# web_fetcher.py for fetching additional information from a web API.

# File Handling
# Create a text file named data.txt with the following content:
# Alice,30
# Fiona,28
# Jasmine,31
# George,33
# Bob,25
# Ella,22
# Hannah,27
# Daniel,40
# Isaac,29
# Charlie,35

# 3. 	Custom Module (do this in file_reader.py):
# Implement a function read_data(file_path) that reads the content from data.txt, parses it, and returns a list of tuples containing names and ages. e..g [("Alice", 30), ("Fiona", 28), ...]
# 4. 	Third-Party Library (do this in web_fetcher.py):
# Use the requests library to fetch data from the public API JSONPlaceholder
# Implement a function fetch_user_data() that retrieves and returns a list of user names from the API.
# 5. 	Main Script:
# 	Create a main script main.py that:
# Imports functions from the file_reader and web_fetcher modules.
# Reads data from data.txt using file_reader.read_data().
# Fetches user data using web_fetcher.fetch_user_data().
# Prints the data from the file and the web.

# 6. 	Before you begin, make sure you:
# Create a virtual environment for your project.
# Install the requests library within this environment.
# Ensure that the virtual environment is used when running your main script.
# Expected Project Structure:
# ├── data_processing
# │   ├── file_reader.py
# │   ├── __init__.py
# │   └── web_fetcher.py
# ├── data.txt
# └── main.py

# Hints:
# For reading files, use Python’s built-in open() function.
# For web requests, use requests.get() from the requests library.
# For package organization, remember to include an empty __init__.py file in the data_processing package directory.
