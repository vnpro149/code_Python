from ncclient import manager
import sys
import xmltodict
import xml.dom.minidom

from device_info import iosxe as device #noqa

# Tao bo loc XML cho truy van NETCONF
netconf_filter = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface></interface>
  </interfaces>
</filter>"""

# Mo ket noi den thiet bi mang bang ncclient
print("Opening NETCONF Connection to {}".format(device["address"]))
with manager.connect(
        host=device["address"],
        port=device["netconf_port"],
        username=device["username"],
        password=device["password"],
        hostkey_verify=False
        ) as m:
# Tao cau truy van NETCONF <get-config> su dung bo loc tren
    print("Sending a <get-config> operation to the device.\n")
    netconf_reply = m.get_config(source = 'running', filter = netconf_filter)

# In ket qua tra ve dang xml
print("Here is the raw XML data returned from the device.\n")
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
#print(netconf_reply)
print("")

# Chuyen ket qua tra ve tu XML sang Dictionary
netconf_data = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]

# Tao danh sach interfaces
interfaces = netconf_data["interfaces"]["interface"]

print("The interface status of the device is: ")
# Chay vong lap cho moi interface va bao cao trang thai
for interface in interfaces:
    print("Interface {} enabled status is {}".format(
            interface["name"],
            interface["enabled"]
            )
        )
print("\n")
