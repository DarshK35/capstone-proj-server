import requests

url = "http://localhost:5000/"

fnc = input("Enter endpoint to test: ")

response = requests.post(url+fnc, data = {"data": [[]]})
print(response.json())