import requests
import json

# Define the URL of your Google Apps Script web app
url = 'https://script.google.com/macros/s/AKfycbwGLcWrSOUviVH6fPV-oLppRw8CJzZDlLLCq9ftUZqiPrcKRyhsVcgpeUex67G4AV9T/exec?action=predictModel'

# Example data for the trainModel function
data = {
	"result": "OK",
	"message": "Predicted on data",
	"predict": 42.5
}

# Convert the data to JSON format
payload = json.dumps(data)

headers = {
	"Content-Type": "application/json"
}

# Send the POST request
response = requests.post(url, data=payload, headers = headers)

# Print the response
print(response.text)