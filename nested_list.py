students = [
            ['Harsh', 20],
            ['Beria', 20],
            ['Varun', 19],
            ['Kakunami', 19],
            ['Vikas', 21]
            ]


students.sort(key = lambda x: x[1])
print(students)
second = students[1][1]
penult = []
for student in students:
    if student[1] == second:
        penult.append(student[0])

penult.sort()

"""
for student in penult:
    print(student)
"""