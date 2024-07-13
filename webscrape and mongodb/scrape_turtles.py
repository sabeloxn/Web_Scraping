#//---------------------------------------------------------------------------------+
#// Finding Elements by Class                                                       +
#//---------------------------------------------------------------------------------+
import requests
from bs4 import BeautifulSoup  # type: ignore
import json

# Making a GET request
r = requests.get('https://en.wikipedia.org/wiki/List_of_Testudines_families')
# check status code for response received
print(r.status_code)
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())
#--END

#Content
table = soup.find('table', class_="wikitable")
# print(s)
keys = []
keys_count=0
headings = table.find_all('th')
for line in headings:
    if keys_count > 11:
        break
    key=line.text
    # print(line.text)
    keys.append(key)
    keys_count +=1
# print("Keys Created:")
# print(keys)

# rows = table.find_all("tr")
# for line in rows:
#     print(line.text)

values = []
columns = table.find_all("tr")
values_count =0
for line in columns:
    if values_count > 11:
        break
    value = line.text
    # print(line.text)
    values.append(value)
    values_count +=1
# print("Values Found:")
# print(values)

#try to get images using child element
# columns = table.find_all("td")
# for line in columns:
#     print(line.text)
#     print(line.img)
#     images = table.find_all("img", class_="mw-file-element",src=True)
#     for image in images:
#         print(image['src'])

# images = table.find_all("img", class_="mw-file-element",src=True)
# for line in images:
#     print(line['src'])
#keys and values simultaneously
# create dictionary
def create_dictionary(keys, values):
    result = {} # empty dictionary
    for key, value in zip(keys, values):
        result[key] = value
    return result

# use create_dictionary func.
# Store JSON data in API_Data 
data = create_dictionary(keys=keys, values=values) 
  
# Print json data using loop 
for key in data:{ 
    #print(key,":", API_Data[key]) #actually readable mode
    print(json.dumps(data, indent=4, sort_keys=True)) #satisfying print :) 
}
# print(create_dictionary(keys=keys, values=values))