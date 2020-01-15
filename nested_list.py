students = [
            ['Harsh', 20],
            ['Beria', 20],
            ['Varun', 19],
            ['Kakunami', 19],
            ['Vikas', 21]
            ]
scores = [i[1] for i in students]
for i in scores:
    times = scores.count(i)
    if times > 1:
        for _ in range(times-1):
            scores.remove(i)

scores.sort()
second = scores[1]
penult = []
for student in students:
    if student[1] == second:
        penult.append(student[0])

for student in sorted(penult):
    print(student)