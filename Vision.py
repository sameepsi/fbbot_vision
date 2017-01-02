'''
Created on 29-Dec-2016

@author: Sameep
'''
from oauth2client.client import GoogleCredentials
from googleapiclient import discovery
from GoogleCloud import getCredentials
import base64
import urllib2
import cStringIO
import json

def get_vision_service():
    # credentials=GoogleCredentials.get_application_default()
    #if credentials is None:
    credentials=getCredentials()
    return discovery.build('vision', 'v1', credentials=credentials)

def detect_face(image_URL,max_result=30):
    image_file=cStringIO.StringIO(urllib2.urlopen(image_URL).read())
    batch_request=[{
        'image':{
            'content':base64.b64encode(urllib2.urlopen(image_URL).read()).decode('utf-8')
            },
        'features':[{
            'type':'FACE_DETECTION',
            'maxResults':max_result
            }]
        }
        ]
    service=get_vision_service()
    request=service.images().annotate(body={
        'requests':batch_request
        })
    response=request.execute()
    jsonData=json.load(response)
    if "responses" not in jsonData:
        return None
    if "faceAnnotations" not in jsonData["responses"][0]:
        return None
    return response["responses"][0]["faceAnnotations"]
    
    
    

