
import requests
from ClimateOPCUAClient.opcuaClient import get_climate_data
from dobotControls.dobotControl import scan_color_move_arm

response = requests.get("https://api.awattar.at/v1/marketdata")
responseObject = eval(response.text)
currentData = responseObject["data"][0]
print(scan_color_move_arm())
temperature, humidity = get_climate_data()

print(currentData)
print(temperature)
print(humidity)
