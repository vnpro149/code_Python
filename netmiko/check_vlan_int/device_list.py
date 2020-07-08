from getpass import getpass
#passwd=getpass("Nhap mat khau SSH: ")
passwd="123"
sw1 = {
    "device_type":"cisco_ios",
    "ip":"192.168.225.138",
    "username":"admin",
    "password":passwd,
    "secret":"321"
    }
sw2 = {
    "device_type":"cisco_ios",
    "ip":"192.168.225.135",
    "username":"admin",
    "password":passwd,
    "secret":"321"
    }
sw3 = {
    "device_type":"cisco_ios",
    "ip":"192.168.225.136",
    "username":"admin",
    "password":passwd,
    "secret":"321"
    }
sw4 = {
    "device_type":"cisco_ios",
    "ip":"10.215.26.233",
    "username":"admin",
    "password":passwd,
    "secret":"321"
}
sw5 = {
    "device_type":"cisco_ios",
    "ip":"10.215.26.233",
    "username":"admin",
    "password":passwd,
    "secret":"321"
    }
device_list=[sw1]