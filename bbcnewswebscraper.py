# This program uses the requests library to make a GET request to the BBC News website and retrieve the HTML content of the page. 
# It then uses the BeautifulSoup library to parse the HTML and search for elements with the class gs-c-promo-heading, which represents the headlines of the latest news articles. 
# Finally, it extracts the text from each headline and prints it to the console.

import requests
import sys
from bs4 import BeautifulSoup
from contextlib import redirect_stdout
from datetime import datetime

# Get the current date and time
now = datetime.now()

# Prints the current date and time in YYYY-MM-DD HH:MM:SS format
print("BBC News articles as of current date and time (YYYY-MM-DD HH:MM:SS):", now)
print('________________________________________________________')


# Make a GET request to the URL
url = "https://www.bbc.com/news"
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")

# Find all the elements with the class 'gs-c-promo-heading'
headlines = soup.find_all("a", class_="gs-c-promo-heading")

# Extract the text from each headline
for headline in headlines:
    print(headline.text.strip() + '\n')

# Opening a file to write the output to from BBC News
with open('bbcnewsheadlines.txt', 'r+') as f:
    # Loop over the headline links and write them to the file
    for headline in headlines:
        f.write(headline.text.strip() + '\n')