import requests
import json

settings = json.loads(open("appSettings.json", "r").read())

def RefreshDataset() -> dict:
	try:
		resultStatus = {}

		url = settings["appScriptUrl"] + "getData"

		if url is None:
			resultStatus["result"] = "ERR"
			resultStatus["message"] = "No URL specified in configuration file"
			return resultStatus
		
		response = requests.get(url)
		if not response.ok:
			raise ValueError("Invalid response/request")

		with open(settings["dataPath"], "w") as file:
			file.write(response.text)

		resultStatus["result"] = "OK"
		resultStatus["message"] = "Dataset synced successfully"
	except Exception as ex:
		resultStatus["result"] = "ERR"
		resultStatus["message"] = str(ex)

	return resultStatus

def SendRequestToAppScript(functioo: str, payload: dict):
	url = settings["appScriptUrl"] + function

	data = json.dumps(payload)
	response = requests.post(url, data = data)
	return response
