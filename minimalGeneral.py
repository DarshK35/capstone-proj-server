def RefreshDataset() -> bool:
	import requests
	import json

	try:
		resultStatus = {}

		settings = json.loads(open("appSettings.json", "r").read())
		url = settings["dataUrl"]

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
