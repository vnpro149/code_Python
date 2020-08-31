import requests
import json
import sys

import meraki_info

def get(base_url=meraki_info.base_url,api='',params=''):
    headers = {"X-Cisco-Meraki-API-Key": meraki_info.api_key}
    url = base_url + api
    print("\nExecuting GET '%s'\n"%url)
    try:
        resp = requests.get(url,headers=headers,params=params)
        print("GET '%s' status" %api,resp.status_code,'\n')
        return(resp)
    except:
        print("Something wrong",api)
        sys.exit()

def post(base_url=meraki_info.base_url, api='', params=''):
    headers = {"content-type" : "application/json","X-Cisco-Meraki-API-Key": meraki_info.api_key}
    url = base_url + api
    print ("\nExecuting POST '%s'\n"%url)
    try:
        resp= requests.post(url,json.dumps(params),headers=headers)
        print ("POST '%s' Status: "%api,resp.status_code,'\n')
        return(resp)
    except:
       print ("Something wrong with POST /",api)
       sys.exit()
       
def put(base_url=meraki_info.base_url,api='',params=''):
    headers = {"X-Cisco-Meraki-API-Key": meraki_info.api_key}
    url = base_url + api
    print("\nExecuting PUT '%s'\n"%url)
    try:
        resp = requests.put(url,headers=headers,params=params,verify=False)
        print("PUT '%s' status" %api,resp.status_code,'\n')
        return(resp)
    except:
        print("Something wrong",api)
        sys.exit()

def delete(base_url=meraki_info.base_url,api='',params=''):
    headers = {"content-type" : "application/json","X-Cisco-Meraki-API-Key": meraki_info.api_key}
    url = base_url + api
    print ("\nExecuting DELETE '%s'\n"%url)
    try:
        resp= requests.delete(url,headers=headers,params=params,verify = False)
        print ("DELETE '%s' Status: "%api,resp.status_code,'\n')
        return(resp)
    except:
       print ("Something wrong with DELETE /",api)
       sys.exit()
       
