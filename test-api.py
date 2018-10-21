
#
# Example of logging in with a Curl call and getting a token
# https://predix-toolkit.run.aws-usw02-pr.ice.predix.io/#!/clientLogin
#


import requests
import base64
import json


client_id = 'a4028f56-2e1c-e4da-d6a7-a7f1eb600801'
client_name = 'SDRDL' 
secret = "838dZk-'C."

uua_url = 'https://624eff02-dbb1-4c6c-90bc-fa85a29e5fa8.predix-uaa.run.aws-usw02-pr.ice.predix.io'

def get_token(uaa, client, secret):
    
   cs = (client + ':' + secret).encode('ascii')
    
   credentials = base64.b64encode(cs) 
   
   headers = {
       'Content-Type': 'application/x-www-form-urlencoded',
       'Cache-Control': 'no-cache',
       'Authorization': b'Basic ' + credentials
       }
   params = {
       'client_id': client,
       'grant_type': 'client_credentials'
   }
   response = requests.post(uaa, headers=headers, data=params)
   
   return json.loads(response.text)['access_token']
   
token = get_token(uua_url+'/oauth/token', client_id, secret)


#
#  Only useful documentation:
# https://www.programmableweb.com/news/how-ge-current-apis-power-smart-city-applications/sponsored-content/2016/07/21?page=2
# 


metadata_url = 'https://ic-metadata-service-sandiego.run.aws-usw02-pr.ice.predix.io'


bbox = '32.715675:-117.161230,32.708498:-117.151681'



def get_assets(url, zone, bbox, device_type):
   url = url + '/v1/assets/search'
   
   headers = {
      'Authorization': 'Bearer ' + token,
      'Predix-Zone-Id': zone
      }
   
   params = {
       'q': 'device-type:' + device_type,
       'bbox': bbox,
       }
   response = requests.get(url, headers=headers, params=params)
   return json.loads(response.text)['_embedded']['assets']





print(get_assets(metadata_url, ))