#//---------------------------------------------------------------------------------+
#// Finding Elements by Class                                                       +
#//---------------------------------------------------------------------------------+
import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# check status code for response received
# success code - 200
print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
#print(soup.prettify())
#--END

# Find all the div having class as article-page_flex.
# The content of the page is under the <p> tag. 
# Now we have to find all the p tags present in this class. 
# We can use the find_all class of the BeautifulSoup.

s = soup.find('div', class_='article-page_flex')
content = s.find_all('p')
#testing on onter elements
# s = soup.find('div', class_='article-title')
# content = s.find_all('h1')
# s = soup.find('div', class_='article-page_flex')
# content = s.find_all('p', dir='ltr')

#-- function region
# Getting the title tag
#print(soup.title)

# Getting the name of the tag
#print(soup.title.name)

# Getting the name of parent tag
#print(soup.title.parent.name)

# use the child attribute to get 
# the name of the child tag
#-- end region
#print(content)

#//---------------------------------------------------------------------------------+
#//Extracting Text from the tags                                                    +
#//---------------------------------------------------------------------------------+

# for line in content:
#     print(line.text)

#the titles on the page
# s = soup.find('div', class_='article-page_flex')
# content = s.find_all('p', dir='ltr')

# for line in content:
#      print(line.text)
#      print()

#just the title
#print(soup.title.text)

#left bar  
# s = soup.find('div', class_='article-page_flex')
# Getting the leftbar
# leftbar = s.find('ul', class_='leftBarList')
# All the li under the above ul
# lines = leftbar.find_all('li')

# for line in lines:
#     print(line.text)

#left bar hyperlinks
s = soup.find('div', class_='article-page_flex')
# Getting the leftbar
leftbar = s.find('ul', class_='leftBarList')
# All the li under the above ul
lines = leftbar.find_all('a', href=True)

# for line in lines:
#     print(line['href'])
 
#//---------------------------------------------------------------------------------+
#//Schedule                                                                         +
#//---------------------------------------------------------------------------------+
import schedule 
import time 
def func(): 
    for line in lines:
        print(line['href'])

schedule.every(5).seconds.do(func) 

while True: 
    schedule.run_pending() 
    time.sleep(1) 