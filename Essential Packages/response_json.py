# import requests module 
import requests 
import json #for the pretty print
# Making a get request 
response = requests.get('https://api.github.com') 
# print response 
print(response) 
print()
# print json content 

#print(response.json()) #advanced reader mode

#//---------------------------------------------------------------------------------+
#//Convert Request Response to Dictionary in Python                                 +
#//---------------------------------------------------------------------------------+

# Store JSON data in API_Data 
API_Data = response.json() 
  
# Print json data using loop 
for key in API_Data:{ 
    #print(key,":", API_Data[key]) #actually readable mode
    print(json.dumps(API_Data, indent=4, sort_keys=True)) #satisfying print :) 
}