from input_to_file import inputs


def main():
    classes, names, surnames, tasks, grades = inputs()
    txt_file = open('message.txt', 'r')
    message = txt_file.read()
    txt_file.close()

    for clas, name, surname, task, grade in zip(classes, names, surnames, tasks, grades):
        print(message.format(clas, name, surname, task, grade, int(grade) + 1))


if __name__ == '__main__':
    main()