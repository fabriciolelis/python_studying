if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    grades = []
    grades = student_marks.get(query_name)
    n = 0
    for i in range(0, len(grades)):
        n += grades[i]
    average = n / 3
    print('{:.2f}'.format(average))