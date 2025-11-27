import csv

def read_csv(list_, file):
    with open(file, mode="r") as doc:
        csv_reader = csv.DictReader(doc, delimiter=",")

        for i in csv_reader:
            list_.append(i)

def save_csv(_list,file,headers):
    with open(file,"w") as doc:
        csv_writer = csv.DictWriter(doc,fieldnames=headers)
        csv_writer.writeheader()
        csv_writer.writerows(_list)