import csv

def read_csv(list_, file):
    with open(file, mode="r") as doc:
        csv_reader = csv.DictReader(doc, delimiter=",")

        for i in csv_reader:
            list_.append(i)