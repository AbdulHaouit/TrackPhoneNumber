import phonenumbers
import folium
from first import number
from phonenumbers import geocoder

key = "a923b4c8537041fea933c9bb84ec8069"

samNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(samNumber, "en")
print(yourLocation)

# get service providor
from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)

query = str(yourLocation)

result = geocoder.geocode(query)
#print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lat']

print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start = 9)

folium.Marker([lat, lng],popup=yourLocation).add_to((myMap))

#save map in html

myMap.save("Location.html")