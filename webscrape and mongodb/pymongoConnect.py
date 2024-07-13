# importing the modules
from datetime import date, timedelta, datetime
from pymongo import MongoClient # type: ignore
from bson.objectid import ObjectId # type: ignore

client = MongoClient('mongodb://localhost:27017/')

try:
    database = client.get_database("test")
    planets = database.get_collection("planets")
    # Query for a movie that has the title 'Back to the Future'
    query = { "name": "Uranus" }
    planet = planets.find_one(query)
    planet_name = planet['name']
    surfaceTemperatureC=planet['surfaceTemperatureC']
    mainAtmosphere=planet['mainAtmosphere']
    print(planet)
    print(planet_name)
    print(surfaceTemperatureC['mean'])
    for val in mainAtmosphere:
        print(val)
    client.close()
except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)