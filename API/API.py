import requests
import json

response = requests.get(url="https://v6.exchangerate-api.com/v6/61a6d17ff4f85170fa23faa5/latest/USD")
if response.status_code == 404:
    raise Exception("This resource does not exist")
elif response.status_code == 401:
    raise Exception("You are not authorized to access this resource")
elif response.status_code == 200:
    raw_data = response.json()
    custom_data = {"Currency": raw_data['base_code'],
                   "Date": raw_data['time_last_update_utc'],
                   "Rate": raw_data['conversion_rates']
                   }
    file = open("Exchange Rate Data.json", "w")
    json.dump(custom_data, file, indent=4)
