# Requests Module
# The requests library is used for making HTTP requests to a specific URL and returns the response. Python requests provide inbuilt functionalities for managing both the request and response.

import requests

# Making a GET request
#r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
r = requests.get('https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=')

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)