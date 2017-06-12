import json

with open('city.list.json') as data_file:
    data = json.load(data_file)

city_list = []

for city in range(209579):
    city_list.append(data[city]['name'])




