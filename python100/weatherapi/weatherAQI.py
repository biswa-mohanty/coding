import AQIClass as aqi
import os
import json
import requests


# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=06513FDE-E2EF-43E3-8930-A9976CFB48EF
# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
def requestData(zipcode: int, distance: int):
    url = os.environ.get(
        'AQIURL') + "/aq/observation/zipCode/current/?format=application/json&zipCode=" + str(zipCode) + "&distance=" + str(distance) + "&API_KEY=" + os.environ.get('AQI_APIKEY')
    #url = os.environ.get(
    #   'AQIURL') + "/aq/observation/zipCode/current/?format=application/json&zipCode=" + str(
    #   95051) + "&distance=" + str(30) + "&API_KEY=" + os.environ.get('AQI_APIKEY')
    print(url)



    try:
        api_request = requests.get(url)
        api_response = json.loads(api_request.content)
        root = [aqi.Root.from_dict(k) for k in api_response]
        print(root)
    except Exception as e:
        print(e)


if __name__ == '__main__':

    try:
        zipCode = int(input("Enter the zip code for which you need the AQI: \n"))
        dist = int(input("Enter the distance from the zip code for which you need the AQI, providing an empty value "
                         "will take default of 0: \n"))
        if dist == 0:
            dist = 25
    except ValueError:
        print("Please input integer only...")
    requestData(95051, 30)
