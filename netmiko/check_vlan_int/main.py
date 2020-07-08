from netmiko import ConnectHandler
from multiprocessing import Process
from device_list import device_list as devices #Nhap danh sach  thiet bi ben file device_list voi ten bien la device
from ntc_templates.parse import parse_output
def show_vlan(device,id_vlan):
    ssh=ConnectHandler(**device)
    ssh.enable()
    data=ssh.send_command("show vlan")
    data_parse=parse_output(platform="cisco_ios",command="show vlan",data=data)
    
    '''
    ###data_parse output###
    [{'interfaces': ['Et0/1', 'Et0/2', 'Et0/3'],
    'name': 'default',
    'status': 'active',
    'vlan_id': '1'},
    {'interfaces': [],
    'name': 'fddi-default',
    'status': 'act/unsup',
    'vlan_id': '1002'},
    {'interfaces': [],
    'name': 'token-ring-default',
    'status': 'act/unsup',
    'vlan_id': '1003'},
    {'interfaces': [],
    'name': 'fddinet-default',
    'status': 'act/unsup',
    'vlan_id': '1004'},
    {'interfaces': [],
    'name': 'trnet-default',
    'status': 'act/unsup',
    'vlan_id': '1005'}]
    '''
    vlan={}
    ###Command
    access_int=["int range e0/1-2","switchport access vlan " + id_vlan]
    ###tao ra tu dien co dang vlan={"vlan_ID":"Interfaces"}
    for i in data_parse:
        vlan[i["vlan_id"]]=i["interfaces"]
    ###Tao ham kiem tra interface cua vlan
    try:
        if "Et0/2" and "Et0/1" in vlan[id_vlan]:
            print("vlan {} da duoc gan cac cong e0/1 va e0/2".format(id_vlan))
            ssh.disconnect()
        else:
            print("Vlan {} chua duoc gan cac cong e0/1 va e0/2".format(id_vlan))
            print(ssh.send_config_set(access_int))
            print(ssh.send_command("show vlan br"))
            ssh.disconnect()
    except KeyError: #Neu vlan id ko co trong tu dien vlan o tren se bao loi KeyError
        print("Khong co vlan tien hanh tao vlan va gan cong")
        print(ssh.send_config_set(access_int))
        print(ssh.send_command("show vlan br"))
        ssh.disconnect()
def main():
    id_vlan=input("Nhap vlan muon kiem tra: ")
    for device in devices:
        my_proc=Process(target=show_vlan,args=(device,id_vlan,))
        my_proc.start()
if __name__ == "__main__":
    main()
