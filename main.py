import requests
import datetime

USERNAME = "subhashish"
TOKEN = "Bh@gw#nJ@@ne"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "walking Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"
print(datetime.datetime.today().strftime('%Y%m%d'))
pixel_config = {
    "date": f"{datetime.datetime.today().strftime('%Y%m%d')}",
    "quantity": "7.9",
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)
put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/20220615"
put_config = {
    "quantity": "8.6",
}
# response = requests.put(url=put_endpoint, json=put_config, headers=headers)
# print(response.text)
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/20220615"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)