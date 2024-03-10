
def make_grade(grade):
    if grade == 'A+':
        return 4.5
    elif grade == 'A0':
        return 4.0
    elif grade == 'B+':
        return 3.5
    elif grade == 'B0':
        return 3.0
    elif grade == 'C+':
        return 2.5
    elif grade == 'C0':
        return 2.0
    elif grade == 'D+':
        return 1.5
    elif grade == 'D0':
        return 1.0
    elif grade == 'F':
        return 0.0
subjectGPA = 0.0
subjectHap = 0.0
for i in range(20):
    subject = list(input().split()) 
    if subject[2] == "P":
        continue
    subjectGPA += float(subject[1])*make_grade(subject[2])
    subjectHap += float(subject[1])
if subjectGPA == 0.0 or subjectHap == 0.0:
    grade = 0
else:
    grade = subjectGPA/subjectHap

print(grade)
