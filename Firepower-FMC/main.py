from tabulate import tabulate
from requests.auth import HTTPBasicAuth
import requests
import csv
import json
requests.packages.urllib3.disable_warnings() #Tắt cảnh báo Warning
def get_token(): #Function lấy Token
    server = "https://10.215.26.207" #IP Server
    api_path = "/api/fmc_platform/v1/auth/generatetoken" #Đường dẫn URL Token
    url = server+api_path 
    response = requests.post(url,#Gửi requests POST tạo token với
    auth= HTTPBasicAuth('admin','VnPro@149'),#Username Password được encode base64
    verify=False)
    return response.headers["x-auth-access-token"]#Láy headers của gói response là Token
def import_object(token):#Function thêm Object
    list_object = []
    server = "https://10.215.26.207"
    api_path = "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networks"
    url = server+api_path+'?bulk=true'  #Bulk=true có nghĩa là thêm nhiều object 1 lúc
    with open("object.csv") as data: #Xử lý file CSV
        csv_data = csv.reader(data,delimiter = ',') 
        next(csv_data)  
        for row in csv_data:
            #Cấu trúc file CSV bao gồm
            #name|value|overridable|description|type
            address = {
                "name" : row[0],
                "value" : row[1],
                "overridable" : bool(row[2]), #Kiểu true/false
                "description" : row[3],
                "type": row[4]
            }   
            list_object.append(address)#Them những thông tin vừa xử lý vào List_object
    headers = {
        'Content-Type': 'application/json',
        'X-auth-access-token':token,
    }
    
    response = requests.post(url, #Gửi requests POST
    data=json.dumps(list_object), #Xử lý dữ liệU JSON
    headers=headers, #thêm header vào trường header
    verify=False) #Tắt SSL
    print(response.status_code) #In response code
    if response.status_code == 200 or response.status_code == 200:
        print("Post was successful")
    else:
        print("Something error")
def show_object(token):#Function show object
    list_object = []
    server = "https://10.215.26.207" 
    api_path = "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networks"
    url = server+api_path+'?limit=999'
    headers = {
        'Content-Type': 'application/json',
        'X-auth-access-token':token,
    }
    response = requests.get(url,headers=headers,verify=False)
    data = response.json() #gắn data response sẽ
    for item in data['items']:
        object = [item['name'],item['id']]
        list_object.append(object)
    print(tabulate(list_object,headers=['Name','ID'],tablefmt='fancy_grid')) #Kẻ bảng Name object hiện có
def main():
    token = get_token()
    #Tạo menu yêu cầu người dùng nhập vào
    print("1. Show object \n2. Import object")
    try:
        choice = input("Nhap lua chon cua ban:")
        if choice == "1":
            show_object(token)
        elif choice == "2":
            import_object(token)
        else:
            print("wrong input")
    except KeyboardInterrupt:
        print("\nThoat khoi chuong trinh")
if __name__ == "__main__":
    main()

