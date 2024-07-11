import requests
from bs4 import BeautifulSoup

# Making a GET request
response = requests.get('https://www.scrapethissite.com/pages/simple/')

# check status code for response received
print(response)
# Parsing the HTML
soup = BeautifulSoup(response.content, 'html.parser')

# print(soup.prettify())

# Page Title
page_title = soup.find('div', class_="row")
content = page_title.find_all("h1")
print(page_title.text.strip())

# The countries on the page
countries = soup.find_all('div', class_="col-md-4 country")

# Print countries up to 10
count=0
for line in countries:
     if count==10:
          break
     print(line.text.strip())
     print()
     count+=1
