from netmiko import ConnectHandler
from multiprocessing import Process
from ntc_templates.parse import parse_output
from device_list import devices #Nhap danh sach  thiet bi ben file device_list
def check_ver(device):
    ssh=ConnectHandler(**device)
    data=ssh.send_command("show ver")
    data_dict=parse_output(platform="cisco_ios",command="show ver",data=data)
    '''#Data_dict
    [{'config_register': '0x2102',
    'hardware': ['CSR1000V'],
    'hostname': 'CSR1000V',
    'mac': [],
    'reload_reason': 'Unknown reason',
    'rommon': 'IOS-XE',
    'running_image': 'packages.conf',
    'serial': ['97XPYZH1ERC'],
    'uptime': '1 week, 4 days, 19 hours, 36 minutes',
    'version': '16.12.3'}]
    '''
    for i in data_dict:
        if i["version"] <= "16.12.2":
            print("{} IP {} version hien tai {} can update version".format(i["rommon"],device["ip"],i["version"]))
        else:
            print("{} IP {} version hien tai {} dang o version moi nhat".format(i["rommon"],device["ip"],i["version"]))
    ssh.disconnect()
def main():
    for i in devices:
        proc=Process(target=check_ver,args=(i,))
        proc.start()
if __name__ == "__main__":
    main()