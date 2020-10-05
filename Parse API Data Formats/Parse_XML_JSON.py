import xmltodict
import json

# DU LIEU TRONG FILE XML
with open('user.xml') as file:
    xml_data = file.read()
print("#"*20)
print("Du lieu dinh dang XML:")
print(xml_data)
# XML TO JSON    
xml_dict = xmltodict.parse(xml_data)
print("#"*20)
print(xml_dict)
print("#"*20)
print("Du lieu dinh dang JSON:")
json_data = json.dumps(xml_dict, indent = 4)
print(json_data)

# LAY DU LIEU
print(type(json_data))
print("So id cua user: ", xml_dict["user"]["id"])
#print(xml_dict["user"]["address"]["street"])
print("Dia chi nha thu nhat: ", xml_dict["user"]["address"][0]["street"])
print("Dia chi nha thu hai: ", xml_dict["user"]["address"][1]["street"])

# JSON TO XML
print("\nDu lieu dinh dang XML chuyen tu Dictionary:")
print(xmltodict.unparse(xml_dict, pretty=True))
#Thong bao can co chinh xac chi 1 root
data = {
    "id": "3242",
    "address":[],
    "score": 18.3
    }
print(xmltodict.unparse(data, pretty=True))
