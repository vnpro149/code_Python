import sys
import requests
import json
from tabulate import tabulate

import pgpd

def get_organizations_list():
    resp = pgpd.get(api="/organizations")
    orgs_list = json.dumps(resp.json(), indent=4)
    return orgs_list

def creat_organizations():
    name = input("Nhap ten organization can tao: ")
    params = {
        "name": name
    }
    resp = pgpd.post(api="/organizations", params=params)
    response_json = json.dumps(resp.json(), indent=4)
    return response_json

def get_organization_id():
    org_str = get_organizations_list()
    org_list = json.loads(org_str)
    #name = "Public API Lab"
    #name = "DeLab"
    name = str(input("Nhap ten cua organization can chon: "))
    for org in org_list:
        if org["name"] == name:
            org_id = org["id"]
    return org_id

def get_networks_list():
    org_id = get_organization_id()
    resp = pgpd.get(api="/organizations/{}/networks".format(org_id))
    networks_list = json.dumps(resp.json(), indent=4)
    return networks_list

def creat_network():
    org_id = get_organization_id()
    name = input("Nhap ten network can tao: ")
    params = {
    "name": name,
    "timeZone": "Europe/Amsterdam",
    "tags": "test",
    "type": "wireless"
    }
    resp = pgpd.post(api="/organizations/{}/networks".format(org_id),params=params)
    response_json = json.dumps(resp.json(), indent=4)
    return response_json

def get_network_id():
    network_list = json.loads(get_networks_list())
    name = "Hoanh Ho"
    #name = str(input("Nhap ten cua network can chon:"))
    for network in network_list:
        if network["name"] == name:
            network_id = network["id"]
    return network_id

def get_devices_list():
    network_id = get_network_id()
    resp = pgpd.get(api="/networks/{}/devices".format(network_id))
    devices_list = json.dumps(resp.json(), indent=4)
    return devices_list

def claim_device_into_network():
    network_id = get_network_id()
    #serial format:"Q2XX-XXXX-XXXX"
    params = {"serial":"Q2ED-UNST-FBEK"}
    #params = {"serial":"Q2ED-TRBT-JZSB"} 
    resp = pgpd.post(api="/networks/{}/devices/claim".format(network_id), params=params)
    return resp

def remove_device_from_network():
    network_id = get_network_id()
    serial = "Q2ED-UNST-FBEK"
    resp = pgpd.post(api="/networks/{}/devices/{}/remove".format(network_id,serial))
    return resp

def get_device_serial():
    devices_str = get_devices_list()
    devices_list = json.loads(devices_str)
    serial_list = []
    i = 0
    for device in devices_list:
        i+=1
        serial_list.append([i, device["serial"]])
        #if device["model"].find("MR") != -1:
        #    serial_list.append([i, device["serial"]])
    print(tabulate(serial_list,headers=['number','serial'],tablefmt="rst"))
    choice = int(input("\nChon so thu tu cua thiet bi muon lay serial: "))
    number = 0
    for serial in serial_list:
        number += 1
        if number == choice:
            device_serial = serial[1]
    return device_serial

def get_single_device():
    network_id = get_network_id()
    serial = get_device_serial()
    resp = pgpd.get(api="/networks/{}/devices/{}".format(network_id,serial))
    single_device = json.dumps(resp.json(), indent=4)
    return single_device

def menu():
    print("""
    ##### Meraki API LAB #####
    1. In danh sach cac organization
    2. Tao organization
    3. In danh sach cac network
    4. Tao network
    5. Lay danh sach cac thiet bi trong network
    6. Dua thiet bi vao trong mang
    7. Xoa thiet bi ra khoi mang
    8. Lay thong tin thiet bi
    9. Lay org id    
    0. Thoat chuong trinh
    ########################## """)
    choice = int(input("Nhap so thu tu chuc nang can chon: "))
    return choice

def main():
    while (True):
        choice = menu()
        if choice == 1:
            result = get_organizations_list()
            print(result)
        elif choice == 2:
            result = creat_organizations()
            print(result)
        elif choice == 3:
            result = get_networks_list()
            print(result)
        elif choice == 4:
            result = creat_network()
            print(result)
        elif choice == 5:
            result = get_devices_list()
            print(result)
        elif choice == 6:
            result = claim_device_into_network()
            print(result)
        elif choice == 7:
            result = remove_device_from_network()
            print(result)
        elif choice == 8:
            result = get_single_device()
            print(result)
        elif choice == 9:
            result = get_organization_id()
            print(result)
        elif choice == 0:
            break
        else:
            print("\n***Ban nhap sai, moi nhap lai***")

if __name__ == "__main__":
    sys.exit(main())
