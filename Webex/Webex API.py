import requests
import sys
import Token

url = "https://api.ciscospark.com/v1/"

def get_room(url=url, access_token = Token.access_token):
    url = url + 'rooms'
    headers = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
    queryParams = {"sortBy" : "lastactivity", "max" : "2"}
    response = requests.get(url=url, headers=headers, params=queryParams)

    print("Thong tin ve cac phong chat:")
    print("Status: " + str(response.status_code))
    return response.text

def post_message(url=url, access_token = Token.access_token):
    url = url + 'messages'
    message = input("Nhap tin nhan muon gui:")
    headers = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
    body = {"toPersonEmail" : "hotuanhoanh8@webex.bot", "text" : "" + message}
    response = requests.post(url=url, json=body, headers=headers)

    print("Tin nhan dang gui di...")
    print("Status: " + str(response.status_code))
    if response.status_code == 200:
        print("Tin nhan gui thanh cong")
    else:
        print("Xay ra loi")
    return response.text

def menu():
    print("\n******************************************************\n")
    print("\t\tBai thuc hanh Webex API\nChon chuc nang can thuc hien:")
    print("1.Lay thong tin ve cac phong chat cua token vua nhap")
    print("2.Gui tin nhan")
    print("0.Thoat")
    choice = int(input("Nhap so cua chuc nang muon chon:"))
    print("\n=================================")
    print("Dang xu ly")
    print("=================================\n")
    return choice

def main():
    while True:
        choice = menu()
        if choice == 0:
            print("Thoat chuong trinh")
            break
        elif choice == 1:
            result = get_room()
            print(result)
        elif choice == 2:
            result = post_message()
            print(result)
        else:
            print("Ban nhap so sai, moi chon lai")
            print("========================================")
    
if __name__ == '__main__':
    sys.exit(main())
