import uuid
import datetime
from datetime import timedelta
import random

def register_loan_application(devices_list,loans_list,id,role,user):
    loan_id = str(uuid.uuid4())
    _id = loan_id[:5]
    date = datetime.date(random.randint(2024, 2025),random.randint(1, 12),random.randint(1, 30))
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
                    elif role == "teacher":
                        return_date = timedelta(days=7)
                        loans_list.append({"loan_id":_id,"device_id":devices_list[i]["device_id"],"device_name":devices_list[i]["device_name"],"user":user,"role":"student","date":date,"return_date":date + return_date})
                        print("Loan approved, The loan is going to be for 7 days\n")
                    else:
                        return_date = timedelta(days=10)
                        loans_list.append({"loan_id":_id,"device_id":devices_list[i]["device_id"],"device_name":devices_list[i]["device_name"],"user":user,"role":"student","date":date,"return_date":date + return_date})
                        print("Loan approved, The loan is going to be for 10 days\n")
                    devices_list[i]["current_status"] = "borrow"
                    return
                else:
                    print("The divice is not avaliable\n")
        print("There is not any divice with that Id\n")

def show_loans(loans_list):
    if not loans_list:
        print("There are not loaned devices\n")
    else:
        for i in range(len(loans_list)):
            print(f"Loan Id: {loans_list[i]["loan_id"]} | Device Id: {loans_list[i]["device_id"]} | Device name: {loans_list[i]["device_name"]} | User name: {loans_list[i]["user"]} | User role: {loans_list[i]["role"]} | Date of loan: {loans_list[i]["date"]} | Date to return: {loans_list[i]["return_date"]}\n")

def register_return(loans_list,loan_id,returns_list,devices_list):
    _date = datetime.date.today()
    return_id = str(uuid.uuid4())
    _id = return_id[:5]
    if not loans_list:
        print("There are not loaned devices\n")
    else:
        for i in range(len(loans_list)):
            if loans_list[i]["loan_id"] == loan_id:
                days_used = (_date - loans_list[i]["date"]).days
                if _date > loans_list[i]["return_date"]:
                    delay = (_date - loans_list[i]["return_date"]).days
                    print(f"Return with delay of {delay}, {days_used} used\n")
                    returns_list.append({"return_id":_id,"loan_id":loan_id,"device_id":loans_list[i]["device_id"],"delay":delay,"date_return":_date,"days_borrow":days_used})
                else:
                    delay = 0
                    print(f"Return on time, {days_used} used\n")
                    returns_list.append({"return_id":_id,"loan_id":loan_id,"device_id":loans_list[i]["device_id"],"delay":delay,"date_return":_date,"days_borrow":days_used})
                loans_list.pop(i)
                devices_list[i]["current_status"] = "avaliable"
            else:
                print("There is not a loaned device with this id\n")

def show_return(returns_list):
    if not returns_list:
        print("There are not returned devices\n")
    else:
        for i in range(len(returns_list)):
            print(f"Return Id: {returns_list[i]["return_id"]} | Loan Id: {returns_list[i]["loan_id"]} | Devices Id: {returns_list[i]["device_id"]} | Delay: {returns_list[i]["delay"]} | Date of return: {returns_list[i]["date_return"]} | Days borrowed: {returns_list[i]["days_borrow"]}\n")