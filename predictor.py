# Importing libraries
import pickle

import numpy as np
import pandas as pd

from keras import Sequential
from keras.layers import Dense, Dropout, BatchNormalization
from keras.callbacks import EarlyStopping
from keras.optimizers import Adam

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Importing Dataset
datasetLoc = "Saved/dataset.json"
dataset = pd.read_json(datasetLoc)

print(dataset.dtypes)
print(dataset.shape)

for i in dataset.columns.values:
	print(i)

# Dataset Manipulation and distribution
dataset = dataset.drop(columns = [
	'ID',
	'Vendor_ID',
	'Pickup_Date',
	'Pickup_Time',
	'Dropoff_Date',
	'Dropoff_Time',
], axis = 1)
dataset = dataset.dropna()

features = [
	'Passenger_Count',
	'Pickup_Longitude',
	'Pickup_Latitude',
	'Dropoff_Longitude',
	'Dropoff_Latitude',
	#'Distane_Km'
]
target = 'Price_Taken'

x = dataset[features]
y = dataset[target]

print(x.shape)

xScaler = StandardScaler()
xScaled = xScaler.fit_transform(x.to_numpy())

print(xScaled.max(), xScaled.min())

yScaler = StandardScaler()
yScaled = yScaler.fit_transform(np.array(y).reshape(-1, 1))

print(yScaled.max(), yScaled.min())

xTrain, xTest, yTrain, yTest = train_test_split(
	xScaled,
	yScaled,
	test_size = 0.15
)


# Model Creation
model = Sequential([
	Dense(256, activation='relu', input_shape=(xTrain.shape[1],)),
	BatchNormalization(),
	Dropout(0.2),
	Dense(512, activation='relu'),
	BatchNormalization(),
	Dropout(0.3),
	Dense(512, activation='relu'),
	BatchNormalization(),
	Dropout(0.3),
	Dense(256, activation='relu'),
	BatchNormalization(),
	Dropout(0.2),
	Dense(1 if len(yTrain.shape) == 1 else yTrain.shape[1])
])
optimizer = Adam(learning_rate = 0.01)
model.compile(optimizer = optimizer, loss = 'mean_squared_error')

# Model Training
earlyStopping = EarlyStopping(
	monitor = 'val_loss',
	patience = 7,
	restore_best_weights = True
)
history = model.fit(
	xTrain,
	yTrain,
	epochs = 250,
	batch_size = 256,
	validation_split = 0.1,
	callbacks = [earlyStopping]
)

# Model Evaluation
loss = model.evaluate(xTest, yTest)
print("Testing Loss:", loss)

saveDir = "Saved/trained_model.keras"
model.save(saveDir)

with open("Saved/xScaler.pkl", "wb") as file:
	pickle.dump(xScaler, file)
with open("Saved/yScaler.pkl", "wb") as file:
	pickle.dump(yScaler, file)