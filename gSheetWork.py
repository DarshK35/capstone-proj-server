import os
import numpy
import pandas

from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def Authenticate():
	cred = None

	if(os.path.exists("token.json")):
		cred = Credentials.from_service_account_file("token.json", scopes = SCOPES)

	print(cred)
	print(cred.valid)

	service = build('sheets', 'v4', credentials=cred)
	print(service)


Authenticate()