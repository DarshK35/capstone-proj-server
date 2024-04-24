import json
import requests

import pandas as pd

url = "https://capstone-proj-server.onrender.com/"

fnc = input("Enter endpoint to test: ")

if fnc != "predictModel":
	response = requests.post(url+fnc, data = {"data": [[]]})
else:
	data = pd.read_json("Saved/dataset.json")
	data = data[-1]

	response = {"ok": "ok"}

print(response.json())