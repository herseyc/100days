import requests
import datetime as dt

USERNAME = "hersey100days"
TOKEN = "Th1SisMYPr0j3ct!2"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=pixela_endpoint, json=user_parameters)
#print(response.text)

pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Coding",
    "unit": "hours",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

##response = requests.post(url=pixela_graph_endpoint, json=graph_params, headers=headers)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

date = dt.datetime.now()
strdate = date.strftime("%Y%m%d")

update_params = {
    "date": strdate,
    "quantity": "4"
}

#response = requests.post(url=graph_endpoint, json=update_params, headers=headers)
#print(response.text)