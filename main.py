import file_csv

log_in_counter = 3
user_file = "users.csv"
user_credentials = []

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
        else:
            print(f"You have {log_in_counter} attemps more\n")
