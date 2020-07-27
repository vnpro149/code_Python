from device import device_list
import json
import requests 
import sys
import tabulate
from pprint import pprint
requests.packages.urllib3.disable_warnings()

def get_auth_token(ip,user,passwd):
#Tạo 1 jsonObject có 2 key username,password có value tương ứng là uname,pword
    r_json = {
        "username": user,
        "password": passwd
    }
    post_url = "https://{}/api/v1/ticket".format(ip) #khai báo URL để post
    headers = {"Content-Type" : "application/json"} #khai báo headers
    r=requests.post(post_url,data = json.dumps(r_json),headers = headers,verify=False) #gửi requests đến server và gán response vào biến r
        #post là tạo dữ liệu ,post_url là địa chỉ ta muốn gửi đến,
        #json.dumps dùng để mã hóa username và password,
        #verify=False để không xác thực SSL
    r.raise_for_status() # Lấy mã trạng thái, 200 là thành công, 404 là not found
    token = r.json()["response"]["serviceTicket"] #Lấy ticket từ r
        # Trả về giá trị
    return {
            "token" : token
            }
def scan(ip,user,passwd,token):
    ticket=token
    headers = {"Content-type":"application/json","X-Auth-Token": ticket['token']}
    url = "https://{}/api/v1/discovery".format(ip)
    body= {
    "name":"Scan CSR1000V",
    "ipAddressList":"10.215.26.170-10.215.26.175",
    "discoveryType":"Range",
    "snmpROCommunity":"vnpro",
    "snmpRWCommunity":"vnpro",
    "userNameList":["admin"],
    "passwordList":["vnpro@149"],
    "protocolOrder": "ssh"
}
    try:
        resp = requests.post(url,headers=headers,params='',data=json.dumps(body),verify=False)
        print(resp) #In ra trạng thái
    except:
        print("Something wrong")
        sys.exit()
def show_scan(ip,user,passwd,token):
    ticket=token
    headers = {"Content-type":"application/json","X-Auth-Token": ticket['token']}
    url = "https://{}/api/v1/discovery".format(ip)
    resp = requests.get(url,headers=headers,params='',verify=False)
    data=resp.json()["response"]
    list_discover=[]
    #pprint(resp.json()["response"])~
    n=0
    for i in data:
        n+=1
        list_discover.append([n,i["name"],i["ipAddressList"],i["id"]])
        return list_discover
    print(list_discover)
    #print(tabulate(list_discover,headers = ['number','Name','IP Range','ID Job'], tablefmt="rst"))
if __name__ == "__main__":
    for i in device_list:
        token=get_auth_token(**i)
        scan(i['ip'],i['user'],i['passwd'],token)
        #show_scan(i['ip'],i['user'],i['passwd'],token)
