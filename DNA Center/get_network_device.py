from  pgpd import *
from tabulate import *

def network_device_list():
    device = []
    try:
        resp = get(api="network-device")
        status = resp.status_code
        response_json = resp.json()
        device = response_json["response"]
        #print(device)
        #print(json.dumps(device,indent=4))
    except ValueError:
        print ("Something wrong, cannot get network device information")
        sys.exit()

    if status != 200:
        print (resp.text)
        sys.exit()

    if device == [] :
        print ("No network device found !")
        sys.exit()

    device_list = []
    i=0
    for item in device:
        i+=1
        device_list.append([i,item["hostname"],item["managementIpAddress"],item["type"],item["instanceUuid"]])
    return (device_list)

result = network_device_list()
print (tabulate(result, headers=['number','hostname','ip','type'],tablefmt="rst"))
