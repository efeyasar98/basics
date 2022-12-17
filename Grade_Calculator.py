def grade_calculate(row_):
    row_ = row_[:-1]

    list1 = row_.split(",")

    student_name = list1[0]

    note1 = int(list1[1])

    note2 = int(list1[2])

    note3 =int(list1[3])

    last_grade = note1 * (3/10) + note2 * (3/10) + note3 * (4/10)

    if (last_grade >= 90):
        grade_ = "AA"
    elif (last_grade >= 80):
        grade_ = "BB"
    elif (last_grade >= 70):
        grade_ = "CC"
    elif (last_grade >= 60):
        grade_ = "DD"
    else:
        grade_ = "FF"

    return student_name + "-------------->" + grade_ + "\n"


    print(list1)


with open("student_grades.txt","r",encoding="utf-8") as file:

    adding_list = []

    for i in file:

        adding_list.append(grade_calculate(i))

    with open("letter_grades.txt","w",encoding="utf-8") as file2:

        for i in adding_list:
            file2.write(i)
