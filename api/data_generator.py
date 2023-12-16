import csv
import random
# read csv file to a list of dictionaries
with open('api/dataset1.csv', 'r', encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)
    data = [row for row in csv_reader]

feedback_dictionary = {
    'Негативний': 0,
    'Нейтральний': 1,
    'Позитивний': 2
}
def get_marks():
    marks = []
    for i in range(0,3):
        row_number = random.randrange(0, len(data), 1)
        feedback_grade = feedback_dictionary.get(data[row_number]["Оцінка фідбека"])
        marks.append({"Lesson":data[row_number]["Предмет"], "Teacher's feedback": feedback_grade, "Grade": data[row_number]["Оцінка"]})
    return marks

