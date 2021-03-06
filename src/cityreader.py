# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.
import csv, os

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# Use Python's built-in "csv" module to read this file so that each record is
# imported into a City instance. (You're free to add more attributes to the City
# class if you wish, but this is not necessary.) Google "python 3 csv" for
# references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.

#Get current working directory
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

#open csv file and save content into csvContent
with open(os.path.join(__location__, 'cities.csv'), newline='') as f:
    content = csv.reader(f, delimiter=',')
    csvContent = list(content)


#Define class City
class City:
    def __init__(self, name, lat, lon, population):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.population = population

#Find index of city name, latitude, longitude, population
nameIdx = csvContent[0].index('city')
latIdx = csvContent[0].index('lat')
lonIdx = csvContent[0].index('lng')
populationIdx = csvContent[0].index('population')

#Create list of City objects
cities = [City(row[nameIdx], row[latIdx], row[lonIdx], row[populationIdx]) for row in csvContent[1:]]

# Print the list of cities (name, lat, lon), 1 record per line.
for i in cities:
    print(i.name, i.lat, i.lon, i.population)


# *** STRETCH GOAL! ***
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Output the cities that fall
# within this square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO
lat1 = input('Enter lat1: ')
lon1 = input('Enter lon1: ')
lat2 = input('Enter lat2: ')
lon2 = input('Enter lon2: ')

result = []
if lat1 > lat2:
    lat1, lat2 = lat2, lat1
if lon1 > lon2:
    lon1, lon2 = lon2, lon1

result = [c for c in cities if lat1<=c.lat<=lat2 and lon1<=c.lon<=lon2]
for i in result:
    print(i.name, i.lat, i.lon)
