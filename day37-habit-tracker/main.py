import requests
from datetime import datetime

USERNAME = "shiroichii"
TOKEN = "pixelaart69"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()
# print(today.strftime("%Y%m%d"))

pxl_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pxl_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? 🤖"),
}

response = requests.post(url=pxl_endpoint, json=pxl_config, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20250422"

update_config = {
    "quantity": "2.5"
}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)