import requests
import sys
import json
import click
from tabulate import tabulate
import SD_WAN_INFO
requests.packages.urllib3.disable_warnings()

SDWAN_IP = SD_WAN_INFO.IP
SDWAN_USERNAME = SD_WAN_INFO.USERNAME
SDWAN_PASSWORD = SD_WAN_INFO.PASSWORD


class rest_api_lib:
    def __init__(self, vmanage_ip, username, password):
        self.vmanage_ip = vmanage_ip
        self.session = {}
        self.login(self.vmanage_ip, username, password)

    def login(self, vmanage_ip, username, password):
        """Login to vmanage"""
        base_url_str = 'https://%s:8443/'%vmanage_ip
        login_action = '/j_security_check'
        login_url = base_url_str + login_action
        
        login_data = {'j_username' : username, 'j_password' : password}
        sess = requests.session()        
        login_response = sess.post(url=login_url, data=login_data, verify=False)
    
        if b'<html>' in login_response.content:
            print ("Login Failed")
            #print(login_response.content)
            sys.exit(0)

        self.session[vmanage_ip] = sess

    def get_request(self, api):
        url = "https://%s:8443/dataservice/%s"%(self.vmanage_ip, api)
        #print url
        response = self.session[self.vmanage_ip].get(url, verify=False)
        data = response.content
        return data

    def post_request(self, api, payload, headers={'Content-Type': 'application/json'}):
        url = "https://%s:8443/dataservice/%s"%(self.vmanage_ip, api)
        payload = json.dumps(payload)
        print(payload)

        response = self.session[self.vmanage_ip].post(url=url, data=payload, headers=headers, verify=False)
        data = response.json()
        return data

sdwanp = rest_api_lib(SDWAN_IP, SDWAN_USERNAME, SDWAN_PASSWORD)

@click.group()
def cli():
    pass

@click.command()
def device_list():
    """Retrieve and return network devices list."""
    click.echo("Retrieving the devices.")

    response = json.loads(sdwanp.get_request('device'))
    items = response['data']

    headers = ["Host-Name", "Device Type", "Device ID", "System IP", "Site ID", "Version", "Device Model"]
    table = list()

    for item in items:
        tr = [item['host-name'], item['device-type'], item['uuid'], item['system-ip'], item['site-id'], item['version'], item['device-model']]
        table.append(tr)
    try:
        click.echo(tabulate(table, headers, tablefmt="fancy_grid"))
    except UnicodeEncodeError:
        click.echo(tabulate(table, headers, tablefmt="grid"))

cli.add_command(device_list)

if __name__ == "__main__":
    cli()
