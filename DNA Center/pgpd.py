import json
import sys
import requests
from requests.auth import HTTPBasicAuth

import controller

requests.packages.urllib3.disable_warnings()

def get_X_auth_token(ip=controller.DNAC_IP, ver=controller.VERSION, uname=controller.USERNAME, pword=controller.PASSWORD):
    post_url = "https://"+ip+"/api/system/"+ ver +"/auth/token"
    headers = {'content-type': 'application/json'}
    try:
        r = requests.post(post_url, auth=HTTPBasicAuth(username=uname, password=pword), headers=headers,verify=False)
        r.raise_for_status()
        return r.json()["Token"]
    except requests.exceptions.ConnectionError as e:
        print ("Error: %s" % e)
        sys.exit()

def get(ip=controller.DNAC_IP, ver=controller.VERSION, uname=controller.USERNAME, pword=controller.PASSWORD, api='', params=''):
    token = get_X_auth_token(ip,ver,uname,pword)
    headers = {"X-Auth-Token": token}
    url = "https://"+ip+"/api/"+ver+"/"+api
    print ("\nExecuting GET '%s'\n"%url)
    try:
        resp= requests.get(url,headers=headers,params=params,verify = False)
        print ("GET '%s' Status: "%api,resp.status_code,'\n')
        return(resp)
    except:
       print ("Something wrong with GET /",api)
       sys.exit()

def post(ip=controller.DNAC_IP, ver=controller.VERSION, uname=controller.USERNAME, pword=controller.PASSWORD, api='', data=''):
    token = get_X_auth_token(ip,ver,uname,pword)
    headers = {"content-type" : "application/json","X-Auth-Token": token}
    url = "https://"+ip+"/api/"+ver+"/"+api
    print ("\nExecuting POST '%s'\n"%url)
    try:
        resp= requests.post(url,json.dumps(data),headers=headers,verify = False)
        print ("POST '%s' Status: "%api,resp.status_code,'\n')
        return(resp)
    except:
       print ("Something wrong with POST /",api)
       sys.exit()

def put(ip=controller.DNAC_IP, ver=controller.VERSION, uname=controller.USERNAME, pword=controller.PASSWORD, api='', data=''):
    token = get_X_auth_token(ip,ver,uname,pword)
    headers = {"content-type" : "application/json","X-Auth-Token": token}
    url = "https://"+ip+"/api/"+ver+"/"+api
    print ("\nExecuting PUT '%s'\n"%url)
    try:
        resp= requests.put(url,json.dumps(data),headers=headers,verify = False)
        print ("PUT '%s' Status: "%api,resp.status_code,'\n')
        return(resp)
    except:
       print ("Something wrong with PUT /",api)
       sys.exit()

def delete(ip=controller.DNAC_IP, ver=controller.VERSION, uname=controller.USERNAME, pword=controller.PASSWORD, api='', params=''):
    token = get_X_auth_token(ip,ver,uname,pword)
    headers = {"content-type" : "application/json","X-Auth-Token": token}
    url = "https://"+ip+"/api/"+ver+"/"+api
    print ("\nExecuting DELETE '%s'\n"%url)
    try:
        resp= requests.delete(url,headers=headers,params=params,verify = False)
        print ("DELETE '%s' Status: "%api,resp.status_code,'\n')
        return(resp)
    except:
       print ("Something wrong with DELETE /",api)
       sys.exit()
