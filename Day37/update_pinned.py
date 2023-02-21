import requests
import datetime as dt

USERNAME = "hersey100days"
TOKEN = "Th1SisMYPr0j3ct!2"
GRAPH_ID = "graph1"
pixela_endpoint = f"https://pixe.la/@{USERNAME}"

headers = {
    "X-USER-TOKEN": TOKEN
}

params = {
    "pinnedGraphID": GRAPH_ID
}

response = requests.put(url=pixela_endpoint, json=params, headers=headers)
print(response.text)