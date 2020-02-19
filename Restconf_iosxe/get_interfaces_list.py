import requests
import sys

requests.packages.urllib3.disable_warnings()

HOST = 'ios-xe-mgmt.cisco.com'
PORT = '9443'
USER = 'developer'
PASS = 'C1sco12345'

def get_configured_interfaces():
    """Lay thong tin qua RESTCONF."""
    url = "https://{h}:{p}/restconf/data/ietf-interfaces:interfaces".format(h=HOST, p=PORT)
    #Dat header cho cau truy van restconf
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}
    #Chay phuong thuc get voi url duoc khai bao o tren
    response = requests.get(url, auth=(USER, PASS),
                            headers=headers, verify=False)

    #tra ve du lieu dang text
    return response.text


def main():
    """Simple main method calling our function."""
    interfaces = get_configured_interfaces()

    #In du lieu tra ve
    print(interfaces)

if __name__ == '__main__':
    sys.exit(main())
