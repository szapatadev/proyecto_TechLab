import file_csv, devices, loans, reports

log_in_counter = 3
user_file = "users.csv"
devices_file = "devices.csv"
loans_file = "loans.csv"
returns_file = "returns.csv"
reports_file = "reports.csv"
user_credentials = []
devices_credentials = []
loans_credentials = []
returns_credentials = []

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

            try:
                file_csv.read_csv(devices_credentials,devices_file)
                file_csv.read_csv(loans_credentials,loans_file)
                file_csv.read_csv(returns_credentials,returns_file)
            except FileNotFoundError:
                file_csv.save_csv(devices_credentials,devices_file,["device_id","device_name","category","current_status","date"])
                file_csv.save_csv(loans_credentials,loans_file,["loan_id","device_id","device_name","user","role","date","return_date"])
                file_csv.save_csv(returns_credentials,returns_file,["return_id","loan_id","device_id","delay","date_return","days_borrow"])
            except:
                print("We are solving the errors\n")
            
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
                                    sub_program = int(input("1 - Register a new device\n2 - Show devices\n3 - Remove a device\n4 - Quit\nWhat do you want to do? "))
                                    if sub_program < 1 or sub_program > 5:
                                        print("Please enter a valid value\n")
                                    else:
                                        #--------------------------------------------------------------------------------------------------
                                        if sub_program == 1:
                                            try:
                                                device_name = str(input("Enter the name of the new device: ").lower())
                                                device_category = str(input("Enter the category of the new device: ").lower())
                                                devices.register_device(devices_credentials,device_name,device_category)
                                            except:
                                                print("Please enter a valid value\n")
                                        #--------------------------------------------------------------------------------------------------
                                        elif sub_program == 2:
                                            print("----------------------Devices----------------------")
                                            devices.show_devices(devices_credentials)
                                        #--------------------------------------------------------------------------------------------------
                                        elif sub_program == 3:
                                            device_id = str(input("Enter the id of the device to remove: ").lower())
                                            devices.delete_device(devices_credentials,device_id)
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
                                    sub_program = int(input("1 - Ask for a loan\n2 - Show loaned devices\n3 - Quit\nWhat do you want to do? "))
                                    if sub_program < 1 or sub_program > 3:
                                        print("Please enter a valid value\n")
                                    else:
                                        #--------------------------------------------------------------------------------------------------
                                        if sub_program == 1:
                                            devices.show_devices(devices_credentials)
                                            _id = input("Enter the id of the device to loan: ")
                                            _role = input("What's the role of the loaner? Student/Teacher/Admin ").lower()
                                            _user = input("What's the name of the loaner? ").lower()
                                            if _role == "student" or "teacher" or "admin":
                                                loans.register_loan_application(devices_credentials,loans_credentials,_id,_role,_user)
                                            else:
                                                print("Enter a valid role\n")
                                        #--------------------------------------------------------------------------------------------------
                                        elif sub_program == 2:
                                            loans.show_loans(loans_credentials)
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
                                            loans.show_loans(loans_credentials)
                                            loan_id = str(input("Enter the loan id: ").lower())
                                            loans.register_return(loans_credentials,loan_id,returns_credentials,devices_credentials)
                                        #--------------------------------------------------------------------------------------------------
                                        elif sub_program == 2:
                                            loans.show_return(returns_credentials)
                                        #--------------------------------------------------------------------------------------------------
                                        else:
                                            print("")
                                            break
                                except:
                                    print("Please enter a valid value\n")
                        #--------------------------------------------------------------------------------------------------
                        elif program == 4:
                            reports.reports(devices_credentials,loans_credentials,returns_credentials)
                            while True:
                                try:
                                    sub_program = int(input("1 - Export the monthly reports via CSV\n2 - Export the yearly reports via CSV\n3 - Quit\nWhat do you want to do? "))
                                    if sub_program < 1 or sub_program > 3:
                                        print("Please enter a valid value\n")
                                    else:
                                        #--------------------------------------------------------------------------------------------------
                                        if sub_program == 1:
                                            month = int(input("Of what month you want to make the report, put the number of the month: "))
                                            year = int(input("Enter the year of the month you want to make the report: "))
                                            if (month < 1 or month > 12) or (year < 2000):
                                                print("Please enter a valid value\n")
                                            else:
                                                info = reports.monthly_reports(devices_credentials,loans_credentials,returns_credentials,month,year)
                                                file_csv.save_csv(info,reports_file,["number_devices","number_loans","number_returns"])
                                                print("The report was made sucessfully\n")
                                            #--------------------------------------------------------------------------------------------------
                                        elif sub_program == 2:
                                            year = int(input("Enter the year of the month you want to make the report: "))
                                            if year < 2000:
                                                print("Please enter a valid value\n")
                                            else:
                                                info = reports.yearly_reports(devices_credentials,loans_credentials,returns_credentials,year)
                                                file_csv.save_csv(info,reports_file,["number_devices","number_loans","number_returns"])
                                        #--------------------------------------------------------------------------------------------------
                                        else:
                                            print("")
                                            file_csv.save_csv(devices_credentials,devices_file,["device_id","device_name","category","current_status","date"])
                                            file_csv.save_csv(loans_credentials,loans_file,["loan_id","device_id","device_name","user","role","date","return_date"])
                                            file_csv.save_csv(returns_credentials,returns_file,["return_id","loan_id","device_id","delay","date_return","days_borrow"])
                                            break
                                except:
                                        print("Please enter a valid value\n")
                        else:
                            break
                except:
                    print("Please enter a valid value\n")
        else:
            print(f"You have {log_in_counter} attemps more\n")
