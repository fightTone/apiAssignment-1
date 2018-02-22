#if theres an error try to input first Caps

import requests

address = raw_input("\nenter your location(city/municipality): ")
req = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+ address+"&appid=AIzaSyDrwth50G9B7CX8z3atHzcqmaIM4I2pJ8M")
obj = req.json()

lat = obj ['results'] [0] ['geometry'] ['location'] ['lat']
lon = obj['results'] [0] ['geometry'] ['location'] ['lng']


r=requests.get('http://api.openweathermap.org/data/2.5/weather?lat='+str(lat)+'&lon='+str(lon)+'&appid=68cf80f75e89694b9412f55e86a85d40')
json_object = r.json()
temp_k = float(json_object['main']['temp'])
celcius = temp_k - 273.15

print "\n\ndid you mean: "
print "\nAdress: "+obj ['results'] [0] ['formatted_address'] 

print "longitude: "+ str(lon)
print "latitude: "+str(lat)
print "Direction: "+ obj['results'] [0] ['address_components'] [2] ['long_name']
print "current temperature: "+ str(celcius)+ " degree Celcius"


