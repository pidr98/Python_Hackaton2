import csv

def inputs():
    fieldnames = ['clas','name','surname', 'task', 'grade']

    classes = input("Enter classes separated by commas: ").split(",")
    names = input("Enter names separated by commas: ").title().split(",")
    surnames = input("Enter surnames separated by commas: ").title().split(",")
    tasks = input("Enter tasks counts separated by commas: ").split(",")
    grades = input("Enter grades separated by commas: ").split(",")

    rows = [{
            'clas': classes,
            'name': names,
            'surname': surnames,
            'task': tasks,
            'grade': grades
        }
    ]
    with open('data.csv', 'w', encoding='UTF8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return classes, names, surnames, tasks, grades

def content():
    contentt = []
    csvfile = open('data.csv', 'r')
    reader = csv.reader(csvfile)
    headers = next(reader)
    for row in reader:
        row_data = {key: value for key, value in zip(headers, row)}
        contentt.append(row_data)
    csvfile.close()
    return contentt
