import requests
import json
import sys
from tabulate import tabulate

import pgpd
import get_network_device
import delete_device

def get_device_config():
    id= delete_device.get_device_id()
    try:
        resp = pgpd.get(api="network-device/"+id+"/config")
        status = resp.status_code
        response_json = resp.json()
        r = response_json["response"]
        print(r)
    except:
        print("Something wrong")
        sys.exit()
def get_device_list_interfaces():
    id= delete_device.get_device_id()
    try:
        resp = pgpd.get(api="interface/network-device/"+id)
        status = resp.status_code
        response_json = resp.json()
        r = json.dumps(response_json, indent = 4)
        print(r)
    except:
        print("Something wrong")
        sys.exit()
def main():
    result = get_network_device.network_device_list()
    print(tabulate(result,
                   headers = ['number','hostname','ip','type','mac address','id'], tablefmt="rst"))
    print("Gets the device config: ")
    result2 = get_device_config()
    print("Gets list of interfaces:")
    result3 = get_device_list_interfaces()
    

if __name__ == '__main__':
    sys.exit(main())
