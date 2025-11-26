import uuid
import datetime
from datetime import timedelta

def register_loan_application(devices_list,loans_list,id,role,user):
    loan_id = str(uuid.uuid4)
    _id = loan_id[:3]
    date = datetime.date.today()
    if not devices_list:
        print("There are not devices\n")
    else:
        for i in range(len(devices_list)):
            if devices_list[i]["device_id"] == id:
                if devices_list[i]["current_status"] != "borrow":
                    if role == "student":
                        return_date = timedelta(days=3)
                        loans_list.append({"loan_id":_id,"device_id":devices_list[i]["device_id"],"device_name":devices_list[i]["device_name"],"user":user,"role":"student","date":date,"return_date":date + return_date})
                        print("Loan approved, The loan is going to be for 3 days\n")
                        return
                    elif role == "teacher":
                        return_date = timedelta(days=7)
                        loans_list.append({"loan_id":_id,"device_id":devices_list[i]["device_id"],"device_name":devices_list[i]["device_name"],"user":user,"role":"student","date":date,"return_date":date + return_date})
                        print("Loan approved, The loan is going to be for 7 days\n")
                        return
                    else:
                        return_date = timedelta(days=10)
                        loans_list.append({"loan_id":_id,"device_id":devices_list[i]["device_id"],"device_name":devices_list[i]["device_name"],"user":user,"role":"student","date":date,"return_date":date + return_date})
                        print("Loan approved, The loan is going to be for 10 days\n")
                        return
                else:
                    print("The divice is not avaliable\n")
        print("There is not any divice with that Id\n")
