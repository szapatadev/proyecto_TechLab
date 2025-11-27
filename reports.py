import datetime

def reports(devices,loans,returns):
    devices_reports = len(devices)
    loans_reports = len(loans)
    returns_reports = len(returns)
    print(f"Have {devices_reports} devices registered, {loans_reports} devices are borrowed. And people have made {returns_reports} returns.\n")

def monthly_reports(devices,loans,returns, month, year):
    devices_len = 0
    loans_len = 0
    returns_len = 0
    for i in range(len(devices)):
        if month == devices[i]["date"].month and year == devices[i]["date"].year:
            devices_len += 1
    for i in range(len(loans)):
        if month == loans[i]["date"].month and year == loans[i]["date"].year:
            loans_len += 1
    for i in range(len(returns)):
        if month == returns[i]["date_return"].month and year == returns[i]["date_return"].year:
            returns_len += 1
    reports_list = [{"number_devices":devices_len,"number_loans":loans_len,"number_returns":returns_len}]
    return reports_list

def yearly_reports(devices,loans,returns, year):
    devices_len = 0
    loans_len = 0
    returns_len = 0
    for i in range(len(devices)):
        if year == devices[i]["date"].year:
            devices_len += 1
    for i in range(len(loans)):
        if year == loans[i]["date"].year:
            loans_len += 1
    for i in range(len(returns)):
        if year == returns[i]["date_return"].year:
            returns_len += 1
    reports_list = [{"number_devices":devices_len,"number_loans":loans_len,"number_returns":returns_len}]
    return reports_list