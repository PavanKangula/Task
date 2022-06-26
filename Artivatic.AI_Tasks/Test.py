import json
import requests


result = requests.get("https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22")

#data = result.json()
data = json.loads(result.text)
m = data['list']

print(type(m))

print(m[0]['main']['temp'])











# for m['i']['dt_txt'] in m:
#     print(m['i']['dt_txt'])

# print(m[i]['dt_txt'])
# print(m[1]['dt_txt'])
# print(m[8]['dt_txt'])

# Days = []
# for i m['dt_txt']
#     Days.append(i)
#
# print(Days)
