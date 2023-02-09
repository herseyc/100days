import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

# Get questions from Opentdb API
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]

#for question in data["results"]:
#    question_data.append(question)


