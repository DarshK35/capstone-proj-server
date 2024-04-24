import json
import requests
import subprocess

import pandas as pd

url = "https://capstone-proj-server.onrender.com/"

fnc = input("Enter endpoint to test: ")

if fnc == "predictModel":
	data = pd.read_json("Saved/dataset.json")
	data = data[-1]

	response = requests.post(url + fnc, data = data.to_json())
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