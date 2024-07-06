#//---------------------------------------------------------------------------------+
#//                                                                                 +
#//---------------------------------------------------------------------------------+
# implement custom decoders

# importing the module
import json
from collections import namedtuple

# creating the data
data = '{"name" : "Geek", "id" : 1, "location" : "Mumbai"}'

# making the object
x = json.loads(data, object_hook =
			lambda d : namedtuple('X', d.keys())
			(*d.values()))

# accessing the JSON data as an object
#print(x.name, x.id, x.location)

# As we can see in the above example, the namedtuple is a class, under the collections module. It contains keys that are mapped to some values. In this case, we can access the elements using keys and indexes.
#--END

#//---------------------------------------------------------------------------------+
#//                                                                                 +
#//---------------------------------------------------------------------------------+
# We can also create a custom decoder function, in which we can convert dict into a custom Python type and pass the value to the object_hook parameter
# customDecoder function
def customDecoder(geekDict):
	return namedtuple('X', geekDict.keys())(*geekDict.values())

# creating the data
geekJsonData = '{"name" : "GeekCustomDecoder", "id" : 2, "location" : "Pune"}'

# creating the object
x = json.loads(geekJsonData, object_hook = customDecoder)

# accessing the JSON data as an object
#print(x.name, x.id, x.location)
#--END
#//---------------------------------------------------------------------------------+
#//                                                                                 +
#//---------------------------------------------------------------------------------+

# We can also use SimpleNamespace class from the types module as the container for JSON objects. Advantages of a SimpleNamespace solution over a namedtuple solution: –

# It is faster because it does not create a class for each object.
# It is shorter and simpler.

# importing the module
try:
	from types import SimpleNamespace as Namespace
except ImportError:
	from argparse import Namespace

# creating the data
data = '{"name" : "GeekNamespace", "id" : 3, "location" : "Bangalore"}'

# creating the object
x = json.loads(data, object_hook = lambda d : Namespace(**d))

# accessing the JSON data as an object
print(x.name, x.id, x.location)
