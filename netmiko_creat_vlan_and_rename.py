from netmiko import  ConnectHandler
SW = {
    'device_type': 'cisco_ios',
    'host':   '10.215.26.251',
    'username': 'admin',
    'password': '123',
    'secret':'321'
}

net_connect = ConnectHandler(**SW)
net_connect.enable()

dic={
    '80':'Phong_nhan_su',
    '81':'Phong_Ke_toan',
    '82':'Phong_Kinh_doanh',
    '83':'Phong_Giam_Doc',
    '84':'Phong_Sales'
    }

for n in range(80,85):  
    ins_vlan=['vlan '+str(n),'name '+dic[str(n)],'exit']
    output= net_connect.send_config_set(ins_vlan)
    print(output)
