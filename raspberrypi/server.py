#!/usr/bin/env python3

import json
import requests
import time
from bottle import route, run

@route('/weather')
def weather():
	now = int(time.time())
	lastqueried = getJsonFromFile('time.json')
	last = int(lastqueried['time'])
	difference = now - last
#	if difference > 600:
#		print('current weather data is older than 10 minutes -- fetching from server')
#		getOnlineWeatherData(2934691)
#		f = open('time.json', 'w')
#		try:
#			json.dump({"time": str(now)}, f)
#		finally:
#			f.close()
	# Now return actual weather data
	weatherData = getLocalWeatherData()
	return str(weatherData)#getJsonFromFile('weather.json')

# This function returns a json Object from a specified file
def getJsonFromFile( fileName ):
    data_file = open(fileName)
    data = json.load(data_file)
    return data

def getOnlineWeatherData( cityID ): #Duisburg 2934691
	url = "http://api.openweathermap.org/data/2.5/weather?id=" + str(cityID) +"&APPID=154e9a2853bb39627c17906e69f7a56c&units=metric"
	r = requests.get(url)
	weather = r.json()
	f = open('weather.json', 'w')
	try:
		json.dump(weather, f)
	finally:
		f.close
def getLocalWeatherData():
	data = getJsonFromFile('weather.json')
	return {"temperatur": data["main"]["temp"]}

run(host='localhost', port=3000, debug=True)
