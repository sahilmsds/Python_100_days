import requests
from datetime import datetime
USERNAME = "sahildj17"
TOEKN = "jklhjkghjkl45fghjkloiitu"
GRAPHID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOEKN,
    "username": USERNAME, 
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id":GRAPHID,
    "name": "Being Studious",
    "unit": "min",
    "type": "int",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOEKN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.now()
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "120"
    
}
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data,headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"
update_data = {
    "quantity": "450"
}
# response = requests.put(url=update_endpoint, json=update_data,headers=headers)
# print(response.text)
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/20250724"
response = requests.delete(url=delete_endpoint,headers=headers)
print(response.text)