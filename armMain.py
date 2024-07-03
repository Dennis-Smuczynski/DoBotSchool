
from yaypackage import get_climate_data,connect_dobot
import pip._vendor.requests as requests

while True:
    print("Please select a mode")
    print("Use (1) to start building")
    print("Use (2) to exit")
    selectedMode = input()
    if selectedMode == "1":
        
        answer,scannedColor = connect_dobot()
        if answer == "error no connection":
            print("There was a problem when trying to connect to dobot, please try again")
        else:
            print(answer)
            print(scannedColor)
            temperature, humidity = 60.0,50.0
            #get_climate_data()
            #get_climate_data()
            response = requests.get("https://api.awattar.at/v1/marketdata")
            responseObject = eval(response.text)
            currentData = responseObject["data"][0]
            climateDict = {
                "temperature":float(temperature),
                "humidity":float(humidity)
            }
            collectedDataDict = {
                "color": scannedColor,
                "climate": {"temperature":float(temperature),
                            "humidity":float(humidity)},
                "currentEnergyCost":currentData["marketprice"]
            }
            requests.post("http://82.165.106.209:3000/component", json=collectedDataDict)
              
    else:
        print("Exiting...")
        break
