import requests

BASE_URI = "http://127.0.0.1:5000/"

resp = requests.get(BASE_URI + "joke/any")
print(resp.json())

input()

resp = requests.get(BASE_URI + "jokebyid/31")
print(resp.json())

resp = requests.put(BASE_URI + "joke/programming", {"category" : "programming", "id" : 100, "joke" : "some random programming joke"})
print(resp.json())