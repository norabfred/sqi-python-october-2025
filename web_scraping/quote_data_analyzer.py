import requests
from bs4 import BeautifulSoup

# <!-- Scrape (the first page of) quotes from the site and perform some basic text and author-based analysis.
# Use the demo site: http://quotes.toscrape.com/
# Count total number of quotes
# Count the number of unique authors
# Find the author with the most quotes on the page
# Count how many quotes contain the word “is” (case-insensitive)
# List all tags that appear and how many times each appears -->

url = "http://quotes.toscrape.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("div", class_="quote")
# Count total number of quotes
print(f"The number of quotes is {len(quotes)}")

# Count the number of unique authors
authors = []
for quote in quotes:
    author = quote.find("small", class_="author").text
    authors.append(author)

unique_authors = set(authors)
num_unique_authors = len(unique_authors)
print(num_unique_authors)

# Find the author with the most quotes on the page
author_with_most_quotes = {}

for author in authors:
    if author not in author_with_most_quotes:
        author_with_most_quotes[author] = 1
    else:
       author_with_most_quotes[author] += 1
print(author_with_most_quotes)


# Count how many quotes contain the word “is” (case-insensitive)
quotes = []
for quote in quotes:
    text = quote.find("span", class_="text").text
    quotes.append(text)

num_quotes_with_is = 0
for quote in quotes:
    quote_lower = quote.lower()
    if " is " in quote_lower or quote_lower.startswith("is "):
        num_quotes_with_is += 1
print(num_quotes_with_is)