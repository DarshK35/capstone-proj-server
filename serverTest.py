import json
import requests
import subprocess

import pandas as pd
import random

# url = "https://capstone-proj-server.onrender.com/"
url = "http://localhost:5000/"

fnc = input("Enter endpoint to test: ")

if fnc == "predictModel":
	data = pd.read_json("Saved/dataset.json")
	data = data.iloc[random.randint(0, data.shape[0] - 1), :]

	print(data.to_json())

	response = requests.post(url + fnc, json = data.to_json())
elif fnc == "debugSystem":
	cmd = input("Enter Command: ")
	nArgs = int(input("Enter number of args: "))
	args = [cmd]

	for _ in range(nArgs):
		arg = input("Enter arg: ")
		args.append(arg)

	data = {
		"cmd": args
	}

	print(data)

	options = {
		"Content-type": "application/json"
	}

	response = requests.post(url + fnc, json = data)
	output = response.json()["msg"]
	print(output)
else:
	response = requests.post(url + fnc)

print(response.json())