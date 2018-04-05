if __name__ == '__main__':
    python_students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = []
        student.append(name)
        student.append(score)
        python_students.append(student)
    python_students.sort(key=lambda student: student[1])
    elem = python_students[0][1]
    while elem in [j for i in python_students for j in i]:
        del python_students[0]
    second = python_students[0][1]
    python_students.sort()
    for i in range(len(python_students)):
        if second == python_students[i][1]:
            print(python_students[i][0])