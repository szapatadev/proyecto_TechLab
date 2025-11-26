import datetime
import uuid

def register_device(_list, name, category, current_status):
    current_date = datetime.date.today()
    device_id = str(uuid.uuid4())
    _id = str(device_id[:5])
    _list.append({"device_id":_id,"device_name":name,"category":category,"current_status":current_status,"date":current_date})
    print("Device sucessfully added\n")

def show_devices(_list, thing_search, all):
    if not _list:
        print("There are not devices\n")
    else:
        for i in range(len(_list)):
            if _list[i]["current_status"] == thing_search:
                print(f"Id: {_list[i]["device_id"]} | Name: {_list[i]["device_name"]} | Category: {_list[i]["category"]} | Status: {_list[i]["current_status"]} | Date: {_list[i]["date"]}\n")
            elif all == True:
                print(f"Id: {_list[i]["device_id"]} | Name: {_list[i]["device_name"]} | Category: {_list[i]["category"]} | Status: {_list[i]["current_status"]} | Date: {_list[i]["date"]}\n")

def delete_device(_list, name):
    if not _list:
        print("There are not devices\n")
    else:
        for i in range(len(_list)):
            if _list[i]["device_name"] == name:
                _list.pop(i)
                print("The device was sucessfully removed\n")
                return
        print("There are not devices with that name\n")