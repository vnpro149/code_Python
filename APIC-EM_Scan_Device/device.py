from getpass import getpass
#passwd=getpass("Nhap passwrd: ")
passwd="VnPro@149"
ap_1 = {
    "ip" : "10.215.26.120", #Địa chỉ IP của APIC-EM
    "user" :"admin", # Tên đăng nhập trong APIC-EM
    "passwd":passwd # Mật khẩu của tài khoản APIC-EM
}
ap_2 = {
    "ip" : "10.215.26.121", #Địa chỉ IP của APIC-EM
    "user" :"admin", # Tên đăng nhập trong APIC-EM
    "passwd":passwd # Mật khẩu của tài khoản APIC-EM
}
ap_3 = {
    "ip" : "10.215.26.122", #Địa chỉ IP của APIC-EM
    "user" :"admin", # Tên đăng nhập trong APIC-EM
    "passwd":passwd # Mật khẩu của tài khoản APIC-EM
}

device_list = [ap_1]