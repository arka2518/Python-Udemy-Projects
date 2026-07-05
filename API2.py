import requests
import csv

# response = requests.get(url="https://v6.exchangerate-api.com/v6/61a6d17ff4f85170fa23faa5/latest/USD")
# response.raise_for_status()
# raw_data = response.json()
    
# update_date = raw_data["time_last_update_utc"]
# rates = raw_data["conversion_rates"]

# file = open("Exchange Rate Data.csv", "w", newline="")
# header = ["Currency", "Date", "Rate"]
# writer = csv.DictWriter(file, fieldnames=header)
# writer.writeheader()

# for currency, rate in rates.items():
#     writer.writerow({"Currency": currency,
#                      "Date": update_date,
#                      "Rate": rate
#                      })

# When we use Pandas
import requests
import pandas as pd

response = requests.get(url="https://v6.exchangerate-api.com/v6/61a6d17ff4f85170fa23faa5/latest/USD")
response.raise_for_status()
raw_data = response.json()

data = pd.DataFrame(raw_data["conversion_rates"].items(),
                    columns=["Currency", "Rate"])

data["Date"] = raw_data["time_last_update_utc"]
data.to_csv("Exchange Rate Data.csv", index=False)
print(data.head())