'''
Created on 29-Dec-2016

@author: Sameep
'''
from oauth2client.client import GoogleCredentials
from googleapiclient import discovery
from GoogleCloud import getCredentials

def get_vision_service():
    credentials=GoogleCredentials.get_application_default()
    if credentials is None:
        credentials=getCredentials()
    return discovery.build('vision', 'v1', credentials=credentials)

