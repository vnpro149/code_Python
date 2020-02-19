import requests #Gửi các loại yêu cầu http đến server và nhận response
import json #Là định dạng dữ liệu để truyền và nhận dữ liệu với server
import sys # Để tương tác với hệ thống
from tabulate import tabulate #cung cấp các format bảng

import pgpd #Lấy các phương thức như get_auth_token, get
def network_device_list():
    device =[]
    try:
        resp = pgpd.get(api="network-device") # Lấy thông tin về network-device
        status = resp.status_code #Lấy trạng thái của yêu cầu trên
        response_json = resp.json() #Lấy nội dung json đã mã hóa từ lời đáp lại
        device = response_json["response"] #Gán thông tin từ lời đáp lại vào device
    except:
        print("Something wrong,cannot get network device info")
        sys.exit()
    # Nếu status khác 200(nghĩa là không thành công) thì in lời đáp lại và thoát chương trình
    if status !=200:
        print (resp.text)
        sys.exit()
    # Nếu chuỗi trống thi in ra không có thiết bị được tìm thấy và thoát chương trình
    if device == []:
        print("No network device found")
        sys.exit()

    device_list =[]
    i=0
    #Tạo một vòng lặp để dò từng item và thực hiện gán các giá trị vào device_list
    #item["hostname"] là dò tìm key hostname trong item và lấy ra value
    for item in device:
        i+=1
        device_list.append([i,item["hostname"],item["managementIpAddress"],
                            item["type"],item["instanceUuid"],item["id"]])
    #thư viện tabulate dùng để khi in dữ liệu ra theo format đã được xây dựng sẵn
    return (device_list)
"""
result = network_device_list()
print(tabulate(result,
            headers = ['number','hostname','ip','type','mac address','id'], tablefmt="rst"))
"""
