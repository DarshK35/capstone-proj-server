import json
import pickle

settings = json.loads(open("appSettings.json", "r").read())

def CreateModel():
	from keras import layers
	from keras import Sequential
	from keras.callbacks import EarlyStopping
	from keras.optimizers import Adam

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


def TrainModel():
	import numpy as np
	import pandas as pd

	from keras.models import load_model
	from keras.callbacks import EarlyStopping
	from sklearn.preprocessing import StandardScaler

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
		"epochsTrained": len(history.history["loss"])
	}
	return response



def PredictModel():
	[]