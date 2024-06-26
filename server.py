from flask import Flask, request, jsonify
import minimalGeneral
import minimalPredictor

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

app = Flask("PythonServer 0.2")


@app.route("/createModel", methods = ["POST"])
def CreateModel():
	response = minimalPredictor.CreateModel()
	return jsonify(response)

@app.route("/trainModel", methods = ["POST"])
def TrainModel():
	response = minimalPredictor.TrainModel()
	minimalGeneral.SendRequestToAppScript("trainModel", response)
	return jsonify(response)

@app.route("/predictModel", methods = ["POST"])
def PredictModel():
	try:
		data = request.json
		print(type(data))
		response = minimalPredictor.PredictModel(data)
	except Exception as ex:
		response = {
			"result": "ERR",
			"message": str(ex)
		}
	minimalGeneral.SendRequestToAppScript("predictModel", response)
	return jsonify(response)

@app.route("/refreshDataset", methods = ['POST'])
def RefreshDataset():
	response = minimalGeneral.RefreshDataset()
	return jsonify(response)

@app.route("/debugSystem", methods = ["POST"])
def DebugSystem():
	try:
		from subprocess import check_output
		data = request.json
		response = {
			"result": "OK",
			"msg": check_output(data["cmd"]).decode("utf-8")
		}
	except Exception as ex:
		response = {
			"result": "ERR",
			"message": str(ex)
		}
		
	return jsonify(response)

if __name__ == "__main__":
	app.run(host = "0.0.0.0")