import datetime
import uuid
import random

def register_device(_list, name, category):
    current_date = datetime.date(random.randint(2024, 2025),random.randint(1, 12),random.randint(1, 30))
    device_id = str(uuid.uuid4())
    _id = str(device_id[:5])
    _list.append({"device_id":_id,"device_name":name,"category":category,"current_status":"avaliable","date":current_date})
    print("Device sucessfully added\n")

def show_devices(_list):
    if not _list:
        print("There are not devices\n")
    else:
        for i in range(len(_list)):
            print(f"Id: {_list[i]["device_id"]} | Name: {_list[i]["device_name"]} | Category: {_list[i]["category"]} | Status: {_list[i]["current_status"]} | Date: {_list[i]["date"]}\n")

def delete_device(_list, id):
    if not _list:
        print("There are not devices\n")
    else:
        for i in range(len(_list)):
            if _list[i]["device_id"] == id:
                _list.pop(i)
                print("The device was sucessfully removed\n")
                return
        print("There are not devices with that id\n")