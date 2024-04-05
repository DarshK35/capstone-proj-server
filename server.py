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
	return jsonify(response)

@app.route("/predictModel", methods = ["POST"])
def PredictModel():
	minimalPredictor.PredictModel()
	return jsonify({"result": "OK"})

@app.route("/refreshDataset", methods = ['POST'])
def RefreshDataset():
	response = minimalGeneral.RefreshDataset()
	return jsonify(response)

if __name__ == "__main__":
	app.run(debug = True)