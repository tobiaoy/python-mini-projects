import requests
from pprint import pprint # turns JSON format into a 'word-tree'

API_Key = 'cd39077c3db9a6f4478eaf047f9668af'
city = input('Enter a city: ')
base_url = f'https://api.openweathermap.org/data/2.5/weather?appid={API_Key}&q={city}'

weather_data = requests.get(base_url).json()

pprint(weather_data)