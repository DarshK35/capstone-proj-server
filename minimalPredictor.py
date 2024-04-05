import json
import pickle

import numpy as np
import pandas as pd

settings = json.loads(open("appSettings.json", "r").read())

def CreateModel():
	from keras import layers
	from keras import Sequential
	from keras.optimizers import Adam

	try:
		modelDescriptor = settings["model"]
		
		start = True
		model = Sequential()
		for l in modelDescriptor["layers"]:
			layerClass = getattr(layers, l["type"])
			params = l.get("parameters", {})
			print(params)

			instance = layerClass(**params)

			if start:
				start = False
				instance = layerClass(**params, input_shape = (modelDescriptor["xTrainColumns"],))
				model.add(instance)
			else:
				model.add(instance)

		optimizer = Adam(learning_rate=0.01)
		model.compile(optimizer = optimizer, loss = "mean_squared_error")

		print(model.summary())
		model.save(settings["modelPath"])

		return {
			"result": "OK",
			"message": "Model created successfully"
		}
	except Exception as ex:
		return {
			"result": "ERR",
			"message": str(ex)
		}


def TrainModel():
	from keras.models import load_model
	from keras.callbacks import EarlyStopping
	from sklearn.preprocessing import StandardScaler

	try:
		dataset = pd.read_json(settings["dataPath"])
		dataset = dataset.dropna()

		datasetParams = settings["datasetParams"]

		x = dataset[datasetParams["features"]]
		y = dataset[datasetParams["target"]]

		xScaler = StandardScaler()
		yScaler = StandardScaler()

		xScaled = xScaler.fit_transform(x.to_numpy())
		yScaled = yScaler.fit_transform(np.array(y).reshape(-1, 1))


		model = load_model(settings["modelPath"])
		earlyStopping = EarlyStopping(
			monitor = 'val_loss',
			patience = 7,
			restore_best_weights = True
		)
		history = model.fit(
			xScaled,
			yScaled,
			epochs = settings["model"]["trainEpochs"],
			validation_split = 0.1,
			callbacks = [earlyStopping]
		)

		model.save(settings["modelPath"])
		with open(settings["scalerPath"]["xScaler"], "wb") as file:
			pickle.dump(xScaler, file)
		with open(settings["scalerPath"]["yScaler"], "wb") as file:
			pickle.dump(yScaler, file)
		
		response = {
			"result": "OK",
			"message": "Model trained successfully",
			"trainStatistics": history.history,
			"epochsTrained": len(history.history["loss"]),
			"finalAccuracy": (1 - history.history["val_loss"][-1]) * 100
		}
		return response
	except Exception as ex:
		return {
			"result": "ERR",
			"message": str(ex)
		}


def PredictModel(data: dict):

	[]
