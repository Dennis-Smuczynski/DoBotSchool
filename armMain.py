
from yaypackage import connect_dobot,get_climate_data
import pip._vendor.requests as requests

response = requests.get("https://api.awattar.at/v1/marketdata")
responseObject = eval(response.text)
currentData = responseObject["data"][0]
print(connect_dobot())
temperature, humidity = get_climate_data()

print(currentData)
print(temperature)
print(humidity)
