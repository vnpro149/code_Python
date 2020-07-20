import requests
import json

import controller # Lấy các thông tin về controller

#Tắt tin nhắn cảnh báo;
requests.packages.urllib3.disable_warnings()
'''Tạo hàm để lấy token;
các tham số ip,ver,uname,pword được gắn giá trị đã khai báo ở trên'''
def get_auth_token(ip=controller.APICEM_IP,ver=controller.VERSION,uname=controller.USERNAME,pword=controller.PASSWORD):
#Tạo 1 jsonObject có 2 key username,password có value tương ứng là uname,pword
    r_json = {
        "username": uname,
        "password": pword
    }
    post_url = "https://"+ip+"/api/"+ver+"/ticket" #khai báo URL để post
    headers = {"Content-Type" : "application/json"} #khai báo headers
#try:...except: nghĩa là nếu code xảy ra lỗi ở trong phần try thì thực hiện phần except
    try:
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
    except:
        print("Status: %s" %r.status_code)
        print("Response: %s" %r.text)

ticket=get_auth_token()
print(ticket)

# Tạo hàm get để lấy thông tin
def get(ip=controller.APICEM_IP,ver=controller.VERSION,uname=controller.USERNAME,pword=controller.PASSWORD,api='',params=''):
    ticket = get_auth_token(ip,ver,uname,pword) #Lấy ticket bằng cách gọi hàm
    headers = {"X-Auth-Token": ticket['token']} #Khai báo headers để gắn ticket vào
    url = "https://"+ip+"/api/"+ver+"/"+api
    print("\nExecuting GET '%s'\n"%url) #In ra thông tin để người dùng biết đang lấy dữ liệu
    try:
        #gửi request đến server, resp là lời đáp lại của yêu cầu, get là lấy dữ liệu
        resp = requests.get(url,headers=headers,params=params,verify=False)
        print("GET '%s' status" %api,resp.status_code,'\n') #In ra trạng thái
        return(resp)
    except:
        print("Something wrong",api)
        sys.exit()

def post(ip=controller.APICEM_IP, ver=controller.VERSION, uname=controller.USERNAME, pword=controller.PASSWORD, api='', params=''):
    token = get_auth_token(ip,ver,uname,pword)
    headers = {"content-type" : "application/json","X-Auth-Token": token}
    url = "https://"+ip+"/api/"+ver+"/"+api
    print ("\nExecuting POST '%s'\n"%url)
    try:
        resp= requests.post(url,json.dumps(params),headers=headers,verify = False)
        print ("POST '%s' Status: "%api,resp.status_code,'\n')
        return(resp)
    except:
       print ("Something wrong with POST /",api)
       sys.exit()
       
# Tạo hàm put chỉnh sửa thông tin
def put(ip=controller.APICEM_IP,ver=controller.VERSION,uname=controller.USERNAME,pword=controller.PASSWORD,api='',params=''):
    ticket = get_auth_token(ip,ver,uname,pword)
    headers = {"X-Auth-Token": ticket['token']}
    url = "https://"+ip+"/api/"+ver+"/"+api
    print("\nExecuting PUT '%s'\n"%url)
    try:
        resp = requests.put(url,headers=headers,params=params,verify=False)
        print("PUT '%s' status" %api,resp.status_code,'\n')
        return(resp)
    except:
        print("Something wrong",api)
        sys.exit()

def delete(ip=controller.APICEM_IP,ver=controller.VERSION,uname=controller.USERNAME,pword=controller.PASSWORD,api='',params=''):

    ticket = get_auth_token(ip,ver,uname,pword)
    headers = {"content-type" : "application/json","X-Auth-Token": ticket['token']}
    url = "https://"+ip+"/api/"+ver+"/"+api
    print ("\nExecuting DELETE '%s'\n"%url)
    try:
    # The request and response of "DELETE" request
        resp= requests.delete(url,headers=headers,params=params,verify = False)
        print ("DELETE '%s' Status: "%api,resp.status_code,'\n') # This is the http request status
        return(resp)
    except:
       print ("Something wrong with DELETE /",api)
       sys.exit()
       
