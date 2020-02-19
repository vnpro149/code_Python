import json
import requests
import sys

# Tắt cảnh báo sSL
requests.packages.urllib3.disable_warnings()
#Thong tin cua Router tren sandbox always-on
HOST = 'ios-xe-mgmt.cisco.com'
PORT = '9443'
USER = 'developer'
PASS = 'C1sco12345'
# Xác định cổng management, không cho sửa cấu hình trên cổng này
MANAGEMENT_INTERFACE = "GigabitEthernet1"

# Tạo URL cho cau truy vấn RESTCONF
url_base = "https://{h}:{p}/restconf".format(h=HOST, p=PORT)

#Khai báo headers
headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}

#Hàm lấy danh sách các cổng
def get_configured_interfaces():
    url = url_base + "/data/ietf-interfaces:interfaces"
    response = requests.get(url,auth=(USER, PASS),headers=headers,verify=False)
    
    return response.json()["ietf-interfaces:interfaces"]["interface"]

#Cấu hình ip cổng
def configure_ip_address(interface, ip):
    # RESTCONF URL của cổng
    url = url_base + "/data/ietf-interfaces:interfaces/interface={i}".format(i=interface)

    #Tạo payload để sửa IP
    data = {
        "ietf-interfaces:interface":{
            "name": interface,
            "type": "iana-if-type:ethernetCsmacd",
            "ietf-ip:ipv4":{
                "address":{
                    "ip": ip["address"],
                    "netmask": ip["mask"]
                }
            }
        }
    }
    #Dùng PUT để chỉnh sửa
    response = requests.put(url,auth=(USER, PASS),headers=headers,verify=False,
                            json=data)
    print(response.text)


#Hàm lấy thông tin chi tiết của cổng đã chọn
def print_interface_details(interface):
    url = url_base + "/data/ietf-interfaces:interfaces/interface={i}".format(i=interface)
    response = requests.get(url,auth=(USER, PASS),headers=headers,verify=False)

    intf = response.json()["ietf-interfaces:interface"]
    print("Name: ", intf["name"])
    try:
        print("IP Address: ", intf["ietf-ip:ipv4"]["address"][0]["ip"], "/",
                              intf["ietf-ip:ipv4"]["address"][0]["netmask"])
    except KeyError:
        print("IP Address: UNCONFIGURED")
    print()

    return(intf)

# Hỏi người dùng chọn cổng nào(Nếu chọn cổng Management thì phải chọn lại)
def interface_selection(interfaces):
    sel = input("Bạn muốn cấu hình với cổng nào? ")
    
    while sel == MANAGEMENT_INTERFACE or not sel in [intf["name"] for intf in interfaces]:
        print("INVALID:  Select an available interface.")
        print("          " + MANAGEMENT_INTERFACE + " is used for management.")
        print("          Choose another Interface")
        sel = input("Bạn muốn cấu hình với cổng nào? ")

    return(sel)


#Yêu cầu người dùng nhập IP và Mask
def get_ip_info():
    ip = {}
    ip["address"] = input("Nhập IP address: ")
    ip["mask"] = input("Nhập subnet mask: ")
    return(ip)


def main():
    #Lấy danh sách các cổng
    interfaces = get_configured_interfaces()

    print("Router có những cổng sau: \n")
    for interface in interfaces:
        print("  * {name}".format(name=interface["name"]))
    print("")

    #Hỏi user chọn cổng nào
    selected_interface = interface_selection(interfaces)
    print(selected_interface)

    #In ra thông tin của cổng đã chọn
    print("Thông tin cổng hiện tại:")
    print_interface_details(selected_interface)

    #Yêu cầu người dùng nhập IP và Mask
    ip = get_ip_info()

    #Gửi cấu hình cổng lên server
    configure_ip_address(selected_interface, ip)

    #In kết quả
    print("Thông tin cổng sau cấu hình:")
    print_interface_details(selected_interface)


if __name__ == '__main__':
    sys.exit(main())
