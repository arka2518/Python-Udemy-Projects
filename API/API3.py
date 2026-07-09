import requests
from datetime import datetime

Username = "bhattacharyaarka2007"
Token = "qwertyfghtfgdbckjfhgkarkahvc"
Graph_ID = "graph4"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {"token" : Token,
               "username" : Username,
               "agreeTermsOfService" : "yes",
               "notMinor" : "yes"
               }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{Username}/graphs"
graph_params = {"id" : Graph_ID,
                "name" : "Consistency Graph",
                "unit" : "Hrs",
                "type" : "int",
                "color" : "shibafu"
                }
headers = {"X-USER-TOKEN" : Token}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

today = datetime.now()

post_endpoint = f"{pixela_endpoint}/{Username}/graphs/{Graph_ID}"
post_params = {"date" : today.strftime('%Y%m%d'),
               "quantity" : input("How many hours did you commit to coding today: "),
               }
response = requests.post(url=post_endpoint, json=post_params, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{Username}/graphs/{Graph_ID}/{today.strftime('%Y%m%d')}"
pixel_params = {"quantity" : "1"
                }
# response = requests.put(url=update_endpoint, json=pixel_params, headers=headers)
# print(response.text)

delete_endpoint =f"{pixela_endpoint}/{Username}/graphs/{Graph_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
