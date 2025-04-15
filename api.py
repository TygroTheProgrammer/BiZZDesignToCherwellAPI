import requests
import jmespath
import csv
import os
import json

from dotenv import load_dotenv, dotenv_values

# Get API info from .env file
load_dotenv()

C_BASE_URL = os.getenv("C_BASE_URL")
C_USERNAME = os.getenv("C_USERNAME")
C_PASSWORD = os.getenv("C_PASSWORD")
C_AUTH_URL = os.getenv("C_AUTH_URL")
C_CLIENT_ID = os.getenv("C_CLIENT_ID")
C_BUSINESS_OBJ_ID = os.getenv("C_BUSINESS_OBJ_ID")

B_BASE_URL = os.getenv("B_BASE_URL")
B_CLIENT_SECRET = os.getenv("B_CLIENT_SECRET")
B_AUTH_URL = os.getenv("B_AUTH_URL")
B_CLIENT_ID = os.getenv("B_CLIENT_ID")


# Class Desc: Handles bearer tokens
class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


# Funtion Desc: This function gets the authorization for the Cherwell API
def getCherwellAuth():
   payload = {"grant_type" : "password","client_id" : C_CLIENT_ID,"username" : C_USERNAME,"password" : C_PASSWORD}

    
   # POST API request
   a = requests.post(C_AUTH_URL,data=payload)

   # Format into JSON
   acc = a.json()


   # Create BearerAuth object to handle requests
   access_token = acc["access_token"]
   auth = BearerAuth(access_token)

   return auth

def getBiZZDesignAuth():
    payload = {"grant_type" : "client_credentials", "client_id" : B_CLIENT_ID, "client_secret" : B_CLIENT_SECRET}

    # POST API request
    a = requests.post(B_AUTH_URL,params=payload)

    # Format into JSON
    acc = a.json()

    # Create BearerAuth object to handle requests
    access_token = acc["access_token"]
    auth = BearerAuth(access_token)

    return auth




def updateFields():
    
    IDtoID = {
        "6158bb0c-7da0-ec11-9dfc-9cb6d0b7310b" : "BiZZDesign"
    }


    # Get all objects
    payload = {"collaborationId" : "repositories/6/collaborations/8", "type" : "ArchiMate:ApplicationComponent", "limit" : "2000"}
    r = requests.get(B_BASE_URL + "/objects", auth=getBiZZDesignAuth(), params=payload)


    bd_objects = r.json()

    # Find BiZZDesign
    bd_obj = jmespath.search(f"_items[?id=='6158bb0c-7da0-ec11-9dfc-9cb6d0b7310b']", bd_objects)

    # Grab all relavent fields
    bd_name = jmespath.search("[*].objectName.en", bd_obj)[0]
    bd_RTO = jmespath.search("[*].documents[?values.dbrecoverytimeobjective].values.dbrecoverytimeobjective | [0]", bd_obj)[0]
    bd_inputs = jmespath.search("[*].documents[?values.dbmajorsysteminputs].values.dbmajorsysteminputs | [0]", bd_obj)[0]
    bd_outputs = jmespath.search("[*].documents[?values.dbmajorsystemoutputs].values.dbmajorsystemoutputs | [0]", bd_obj)[0]
    bd_license_impact = jmespath.search("[*].documents[?values.dblicenseimpact].values.dblicenseimpact | [0]", bd_obj)[0]
    bd_os = jmespath.search("[*].documents[?values.dboperatingsystem].values.dboperatingsystem | [0]", bd_obj)[0]
    
    # Prepare data for upload
    data = {
        "BIZZdesignApplicationName": bd_name,
        "BIZZdesignRTO": bd_RTO,
        "BIZZdesignMajorInputs": bd_inputs,
        "BIZZdesignMajorOutputs": bd_outputs,
        "BIZZdesignLicenseImpact": bd_license_impact,
        "BIZZdesignOperatingSystem": bd_os
    }
    r = requests.patch(C_BASE_URL + "/V1/object/ConfigApplications/BiZZDesign", auth=getCherwellAuth(), json=data)



updateFields()