import file_csv
import devices
import loans

log_in_counter = 3
user_file = "users.csv"
devices_fiel = "devices.csv"
user_credentials = []
devices_credentials = [
    {"device_id":"ab25a","device_name":"laptop","category":"technology","current_status":"avaliable","date":2025-11-25},
    {"device_id":"ac48b","device_name":"laptop","category":"technology","current_status":"borrow","date":2025-11-25}
]
loans_credentials = []

#----------------------------------------------------------------------LOGIN-------------------------------------------------------------------
print("--------------------Log In--------------------")
print("You only have three attemps to log in\n")
file_csv.read_csv(user_credentials,user_file)

while log_in_counter != 0:
    log_in_counter -= 1
    user_ = input("User: ")
    password_ = input("Password: ")
    for i in range(len(user_credentials)):
        if user_credentials[i]["user"] == user_ and user_credentials[i]["password"] == password_:
            print("Sucessfully loged in\n")
            log_in_counter = 0
#----------------------------------------------------------------------MENU-------------------------------------------------------------------
            while True:
                try:
                    program = int(input("1 - Devices management\n2 - Loans\n3 - Returns\n4 - Reports\n5 - Quit\nWhat do you want to do? "))
                    print("")
                    if program < 1 or program > 5:
                        print("Please enter a valid value\n")
                    else:
                        #--------------------------------------------------------------------------------------------------
                        if program == 1:
                            while True:
                                try:
                                    sub_program = int(input("1 - Register a new device\n2 - Show devices\n3 - See loaned/avaliable equipment\n4 - Remove a device\n5 - Quit\nWhat do you want to do? "))
                                    if sub_program < 1 or sub_program > 5:
                                        print("Please enter a valid value\n")
                                    else:
                                        #--------------------------------------------------------------------------------------------------
                                        if sub_program == 1:
                                            try:
                                                device_name = str(input("Enter the name of the new device: ").lower())
                                                device_category = str(input("Enter the category of the new device: ").lower())
                                                current_status = str(input("Enter the current status (Avaliable/Borrow): ").lower())
                                                if current_status == "avaliable" or current_status == "borrow":
                                                    devices.register_device(devices_credentials,device_name,device_category,current_status)
                                                else:
                                                    print("Please enter a valid value\n")
                                            except:
                                                print("Please enter a valid value\n")
                                        #--------------------------------------------------------------------------------------------------
                                        elif sub_program == 2:
                                            print("----------------------Devices----------------------")
                                            devices.show_devices(devices_credentials,"",True)
                                        #--------------------------------------------------------------------------------------------------
                                        elif sub_program == 3:
                                            _do = input("What you want to see the loaned or the avaliable devices? Loaned/Avaliable ").lower()
                                            if _do == "loaned":
                                                print("----------------------Loan Devices----------------------")
                                                devices.show_devices(devices_credentials,"borrow",False)
                                            elif _do == "avaliable":
                                                print("----------------------Devices Avaliable----------------------")
                                                devices.show_devices(devices_credentials,"avaliable",False)
                                            else:
                                                print("Please enter a valid value\n")
                                        #--------------------------------------------------------------------------------------------------
                                        elif sub_program == 4:
                                            device_name = str(input("Enter the name of the device to remove: ").lower())
                                            devices.delete_device(devices_credentials,device_name)
                                        #--------------------------------------------------------------------------------------------------
                                        else:
                                            print("")
                                            break
                                except:
                                    print("Please enter a valid value\n")
                        #--------------------------------------------------------------------------------------------------
                        elif program == 2:
                            while True:
                                try:
                                    sub_program = int(input("1 - Ask for a loan\n2 - Quit\nWhat do you want to do? "))
                                    if sub_program < 1 or sub_program > 3:
                                        print("Please enter a valid value\n")
                                    else:
                                        #--------------------------------------------------------------------------------------------------
                                        if sub_program == 1:
                                            devices.show_devices(devices_credentials,"",True)
                                            _id = input("Enter the id of the book to loan: ")
                                            _role = input("What's the role of the loaner? Student/Teacher/Admin ").lower
                                            _user = input("What's the name of the loaner? ").lower
                                            if _role == "student" or "teacher" or "admin":
                                                loans.register_loan_application(devices_credentials,loans_credentials,_id,_role,_user)
                                            else:
                                                print("Enter a valid role\n")
                                        #--------------------------------------------------------------------------------------------------
                                        else:
                                            print("")
                                            break
                                except:
                                    print("Please enter a valid value\n")
                        #--------------------------------------------------------------------------------------------------
                        elif program == 3:
                            while True:
                                try:
                                    sub_program = int(input("1 - Register return\n2 - Show returns\n3 - Quit\nWhat do you want to do? "))
                                    if sub_program < 1 or sub_program > 3:
                                        print("Please enter a valid value\n")
                                    else:
                                        #--------------------------------------------------------------------------------------------------
                                        if sub_program == 1:
                                            print("Something\n")
                                        #--------------------------------------------------------------------------------------------------
                                        elif sub_program == 2:
                                            print("Something\n")
                                        #--------------------------------------------------------------------------------------------------
                                        else:
                                            print("")
                                            break
                                except:
                                    print("Please enter a valid value\n")
                        #--------------------------------------------------------------------------------------------------
                        elif program == 4:
                            while True:
                                try:
                                    sub_program = int(input("1 - Export the monthly reports via CSV\n2 - Export the yearly reports via CSV\n3 - Quit\nWhat do you want to do? "))
                                    if sub_program < 1 or sub_program > 3:
                                        print("Please enter a valid value\n")
                                    else:
                                        #--------------------------------------------------------------------------------------------------
                                        if sub_program == 1:
                                            print("Something\n")
                                        #--------------------------------------------------------------------------------------------------
                                        elif sub_program == 2:
                                            print("Something\n")
                                        #--------------------------------------------------------------------------------------------------
                                        else:
                                            print("")
                                            break
                                except:
                                    print("Please enter a valid value\n")
                        else:
                            break
                except:
                    print("Please enter a valid value\n")
        else:
            print(f"You have {log_in_counter} attemps more\n")
