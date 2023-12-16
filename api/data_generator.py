import csv
import random
# read csv file to a list of dictionaries
with open('api/dataset1.csv', 'r', encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)
    data = [row for row in csv_reader]


def get_name():
    row_number = random.randrange(0, len(data), 1)
    return data[row_number]["Прізвище"], data[row_number]["Ім'я"]

def get_marks():
    marks = []
    for i in range(0,3):
        row_number = random.randrange(0, len(data), 1)
        marks.append(data[row_number]["Оцінка"])
    return marks

