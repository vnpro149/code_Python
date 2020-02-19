from ncclient import manager
import sys
import xmltodict
import xml.dom.minidom

from device_info import iosxe as device

# Khai bao kieu cong
IETF_INTERFACE_TYPES = {
        "loopback": "ianaift:softwareLoopback",
        "ethernet": "ianaift:ethernetCsmacd"
    }

#Tao template XML cho cong
netconf_interface_template = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
        	<name>{name}</name>
        	<description>{desc}</description>
        	<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
                {type}
            </type>
        	<enabled>{status}</enabled>
        	<ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        		<address>
        			<ip>{ip_address}</ip>
        			<netmask>{mask}</netmask>
        		</address>
        	</ipv4>
        </interface>
    </interfaces>
</config>"""

#Yeu cau nhap thong tin cong Loopback
new_loopback = {}
new_loopback["name"] = "Loopback" + input("What loopback number to add? ")
new_loopback["desc"] = input("What description to use? ")
new_loopback["type"] = IETF_INTERFACE_TYPES["loopback"]
new_loopback["status"] = "true"
new_loopback["ip_address"] = input("What IP address? ")
new_loopback["mask"] = input("What network mask? ")

# Tao Netconf payload chua du lieu cho cong
netconf_data = netconf_interface_template.format(
        name = new_loopback["name"],
        desc = new_loopback["desc"],
        type = new_loopback["type"],
        status = new_loopback["status"],
        ip_address = new_loopback["ip_address"],
        mask = new_loopback["mask"]
    )

print("The configuration payload to be sent over NETCONF.\n")
print(netconf_data)

print("Opening NETCONF Connection to {}".format(device["address"]))

# Tao ket noi den thiet bi bang thu vien ncclient
with manager.connect(
        host=device["address"],
        port=device["netconf_port"],
        username=device["username"],
        password=device["password"],
        hostkey_verify=False
        ) as m:

    print("Sending a <edit-config> operation to the device.\n")
    # tao cau truy van Netconf <get-config> su dung bo loc tren (netconf_data)
    netconf_reply = m.edit_config(netconf_data, target = 'running')

print("Here is the raw XML data returned from the device.\n")
#In ket qua tra ve
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
print("")
