# Capstone Project Server

## Table of Contents
* [Pre-requisites](#pre-requisites)
* [Installation](#installation)
* [Usage](#usage)
* [File Descriptions](#file-descriptions)
* [Configuration](#configuration)
* [Testing](#testing)

## Pre-requisites
Before installing and using this repository, make sure your system running the code satisfies the following requirements:

* **Operating System**: Linux (any distribution, preferably Ubuntu or Arch)
* **GPU**: Nvidia RTX series GPU with at least 6 GB VRAM for running the server locally
* **RAM**: 16 GB minimum

## Installation
1. Install python libraries
	```bash
	pip install numpy pandas tensorflow[and-cuda] scikit-learn flask requests json pickle
	```

1. Clone the repository
	```bash
	git clone https://github.com/DarshK35/capstone-proj-server.git
	```


## Usage
To run the server, run the following command:

```bash
python server.py
```

## File Descriptions
* **`server.py`**: Main server script that handles requests and responses
* **`predictor.py`**: Base script containing logic for creating and handling ML model.
* **`minimalPredictor.py` and `minimalGeneral.py`**: Lightweight scripts for isolating ML model functions in server
* **`serverTest.py`**: Script for testing server API endpoints
* **`appSettings.json`**: Configuration file for setting server and model parameters
* **`Procfile`** Configuration for deploying the server on platforms such as Heroku or Render


## Configuration
The `appSettings.json` file comes with all necessary variables pre-set, and in case of configuration issues, a backup version is also provided in `appSettings.json.bak`

The following things are configured using `appSettings.json`:
* Google Apps Script URL
* Cached Datasset Location
* Dataset feature and target variable definition
* ML Model architecture and Save Path
* ML Model training steps limit
* Dataset scaler save locations

## Testing
When running `server.py`, the following endpoints are active and can be tested:
* `createModel`: Create a fresh ML model
* `trainModel`: Train the model on cached dataset
* `predictModel`: Get a prediction on input data using the model
* `refreshDataset`: Refresh the cached dataset with the Google Sheet data defined by the Google Apps Script
* `debugSystem`: Execute a shell command to ensure server functionality without heavy executions (**DEBUG FUNCTION, SHOULD BE DISABLED FOR PRODUCTION VERSIONS**)


To test the endpoints, use the `serverTest.py` script using the following command:  
```bash
python serverTest.py
```

The endpoint that is to be tested needs to be fully typed when prompted.